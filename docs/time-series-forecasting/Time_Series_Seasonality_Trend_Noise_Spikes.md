
# 📈 Time Series Analysis Reference: Redemption Count (2022–2024)

This guide summarizes the core concepts of time series decomposition and diagnostics using your Toronto Island ferry ticket data. It includes explanations, Python code (with pandas), and plot logic for:

- Seasonality (Yearly, Monthly, Weekly)
- Trend
- Noise
- Spikes (Outliers)

---

## 🔁 Seasonality

Seasonality refers to **repeating patterns** at regular intervals.

### 🔹 Yearly Seasonality
**Definition**: Repeats annually (e.g., summer peaks).
**Detection**: Use STL decomposition with `period=365`.

```python
from statsmodels.tsa.seasonal import STL
stl = STL(df['Redemption Count'], period=365)
res = stl.fit()
res.seasonal.plot(title='Yearly Seasonality')
```

---

### 🔹 Monthly Seasonality
**Definition**: Monthly fluctuation pattern (e.g., ramp-up to summer).
**Detection**: Group by month and take averages.

```python
df['month'] = df.index.month
monthly_avg = df.groupby(df.index.to_period("M"))['Redemption Count'].mean()
monthly_avg.plot(title='Monthly Average Redemption Count')
```

---

### 🔹 Weekly Seasonality
**Definition**: Weekly behavior, like weekend peaks.
**Detection**: Group by `dayofweek` (0=Monday, 6=Sunday)

```python
df['dayofweek'] = df.index.dayofweek
weekly_avg = df.groupby('dayofweek')['Redemption Count'].mean()
weekly_avg.plot(kind='bar', title='Weekly Seasonality (0=Mon)')
```

---

## 📈 Trend

Trend is the **long-term direction** in the data.

### 🔹 Rolling Average (Visual)
```python
df['Redemption Count'].rolling(window=90).mean().plot(title='90-Day Rolling Average (Trend)')
```

### 🔹 STL Decomposition
```python
stl = STL(df['Redemption Count'], period=7)
res = stl.fit()
res.trend.plot(title='Trend Component')
```

---

## 🔀 Noise

Noise = **random small fluctuations** not explained by trend/seasonality.

### 🔹 View residuals (STL)
```python
residual = res.resid
residual.plot(title='Residuals = Noise')
```

### 🔹 Check if noise is normal (±3 std dev)
```python
plt.axhline(residual.mean() + 3 * residual.std(), linestyle='--', color='red')
plt.axhline(residual.mean() - 3 * residual.std(), linestyle='--', color='red')
```

---

## ⚡ Spikes (Outliers)

Spikes = **large, rare deviations** (special events, data errors).

### 🔹 Detect using IQR on residuals:
```python
Q1 = residual.quantile(0.25)
Q3 = residual.quantile(0.75)
IQR = Q3 - Q1
spikes = residual[(residual < Q1 - 1.5 * IQR) | (residual > Q3 + 1.5 * IQR)]
```

### 🔹 Plot on time series:
```python
plt.plot(df['Redemption Count'], label='Redemption Count')
plt.scatter(spikes.index, df.loc[spikes.index, 'Redemption Count'], color='red', label='Spikes')
```

---

## ✅ Summary Table

| Component    | Meaning                                | How to Detect                           |
|--------------|-----------------------------------------|------------------------------------------|
| Yearly Seasonality | Repeats each year                    | STL (`period=365`)                      |
| Weekly Seasonality | Peaks on weekends                   | `groupby(dayofweek).mean()`             |
| Trend         | Long-term growth/decline               | STL trend or 90-day rolling average     |
| Noise         | Small random changes                   | Residuals from STL                      |
| Spikes        | Big, irregular deviations              | Outliers from residual (IQR/z-score)    |

---

This file serves as a compact revision guide and a reproducible analysis script using pandas and matplotlib.

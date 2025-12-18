
# 📈 Time Series Analysis Reference: Redemption Count (2022–2024)

This guide summarizes the core concepts of time series decomposition and diagnostics using your Toronto Island ferry ticket data. It includes explanations, Python code (with pandas), and actual plots for:

- Seasonality (Yearly, Monthly, Weekly)
- Trend
- Noise
- Spikes (Outliers)

---

## 🔁 Seasonality

### 🔹 Yearly Seasonality
Repeats annually (e.g., summer peaks). Detected via STL with `period=365`.

```python
stl = STL(df['Redemption Count'], period=365)
res = stl.fit()
res.seasonal.plot()
```

![Yearly Seasonality](/mnt/data/yearly_seasonality.png)

---

### 🔹 Monthly Seasonality
Average counts per calendar month across years.

```python
monthly_avg = df.groupby(df.index.to_period("M"))['Redemption Count'].mean()
monthly_avg.plot()
```

![Monthly Average](/mnt/data/monthly_avg.png)

---

### 🔹 Weekly Seasonality

Weekday-wise pattern. (0=Mon, 6=Sun)

```python
weekly_avg = df.groupby('dayofweek')['Redemption Count'].mean()
weekly_avg.plot(kind='bar')
```

![Weekly Seasonality](/mnt/data/weekly_avg.png)

---

## 📈 Trend

Trend shows long-term growth or decline.

```python
stl = STL(df['Redemption Count'], period=7)
res = stl.fit()
res.trend.plot()
```

![Trend Component](/mnt/data/trend_component.png)

---

## 🔀 Noise

Noise = residuals after removing trend & seasonality.

```python
residual = res.resid
residual.plot()
```

![Noise (Residuals)](/mnt/data/noise_residuals.png)

---

## ⚡ Spikes (Outliers)

Unusual jumps detected using IQR from residuals.

```python
spikes = residual[(residual < Q1 - 1.5 * IQR) | (residual > Q3 + 1.5 * IQR)]
```

![Spikes Plot](/mnt/data/spikes_plot.png)

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

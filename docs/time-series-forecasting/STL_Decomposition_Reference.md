
# 📊 STL Decomposition using `statsmodels` – Reference Guide

STL stands for **Seasonal-Trend decomposition using LOESS**.  
It is one of the most powerful and interpretable techniques to analyze time series data.

---

## 🔍 What is STL?

STL breaks a time series into three components:

```
Original Series = Trend + Seasonal + Residual
```

| Component   | Description                                  |
|-------------|----------------------------------------------|
| `Trend`     | Long-term direction (e.g., upward/downward) |
| `Seasonal`  | Repeating patterns (e.g., weekly, yearly)   |
| `Residual`  | What's left (noise, spikes, randomness)     |

---

## 🧰 Using STL in `statsmodels`

### ✅ Basic Syntax

```python
from statsmodels.tsa.seasonal import STL

stl = STL(series, period=7)
result = stl.fit()
```

### 📌 Parameters:

| Parameter   | Purpose                                              |
|-------------|------------------------------------------------------|
| `series`    | Your time series (pandas Series with datetime index)|
| `period`    | Length of seasonal cycle (e.g., 7 for weekly)       |

---

## 📈 Accessing Components

```python
trend = result.trend
seasonal = result.seasonal
residual = result.resid
```

You can plot them individually or all together:

```python
result.plot()
plt.suptitle("STL Decomposition of Time Series")
plt.show()
```

---

## ⚙️ Optional Parameters

```python
STL(series, 
    period=7, 
    robust=True, 
    seasonal=13, 
    trend=None, 
    low_pass=None)
```

| Parameter    | Description |
|--------------|-------------|
| `robust`     | Make STL ignore outliers (`True` = recommended) |
| `seasonal`   | Smoothness of seasonal component (higher = smoother) |
| `trend`      | Window size to smooth trend |
| `low_pass`   | Smoothing filter for the combined result |

---

## ✅ Why Use STL?

| Feature                  | STL Strength                              |
|--------------------------|-------------------------------------------|
| Non-constant seasonality | Captures shifting seasonal patterns       |
| Robust to outliers       | With `robust=True`, handles spikes well   |
| Flexibility              | Tune smoothness of trend/seasonality      |
| Interpretable            | Trend, seasonal, and residuals separated  |
| Missing data             | Handles missing values gracefully         |

---

## 🧠 Interpretation Tip

- **Trend** tells you how the data is growing or declining over time
- **Seasonal** helps you understand weekly/yearly cycles
- **Residual** reveals noise and outliers (after removing known patterns)

---

## 📊 Example on Ferry Redemption Count

```python
from statsmodels.tsa.seasonal import STL
import matplotlib.pyplot as plt

stl = STL(df['Redemption Count'], period=7, robust=True)
result = stl.fit()

result.plot()
plt.suptitle("STL Decomposition: Redemption Count")
plt.show()
```

---

Use STL decomposition when your time series has **complex, overlapping patterns** like:
- Seasonal tourism (e.g., summer spikes)
- Weekly behavioral changes (e.g., weekend traffic)
- Long-term growth or decline


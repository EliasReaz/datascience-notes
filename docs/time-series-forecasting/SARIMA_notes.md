Here is a simulated table showing how ARIMA(1,1,1) works step-by-step:

| Date       | Original | Differenced | AR\_Part Calculation | AR\_Part | MA\_Adjustment Calculation            | MA\_Adjustment | ARIMA\_Prediction Calculation | ARIMA\_Prediction |
| ---------- | -------- | ----------- | -------------------- | -------- | ------------------------------------- | -------------- | ----------------------------- | ----------------- |
| 2022-01-01 | 10.00    | NaN         | -                    | NaN      | -                                     | NaN            | -                             | NaN               |
| 2022-01-02 | 11.62    | 1.62        | -                    | NaN      | -                                     | NaN            | -                             | NaN               |
| 2022-01-03 | 11.01    | -0.61       | 0.7 × 1.62           | 1.14     | -                                     | NaN            | -                             | NaN               |
| 2022-01-04 | 10.48    | -0.53       | 0.7 × -0.61          | -0.43    | 0.5 × (-0.61 - 1.14) = 0.5 × -1.75    | -0.87          | -0.43 + (-0.87) = -1.30       | -1.30             |
| 2022-01-05 | 9.41     | -1.07       | 0.7 × -0.53          | -0.37    | 0.5 × (-0.53 - (-0.43)) = 0.5 × -0.10 | -0.05          | -0.37 + (-0.05) = -0.42       | -0.42             |

* **Original**: Raw data values.
* **Differenced**: Change from previous value.
* **AR\_Part Calculation**: Formula used to compute AR\_Part (ϕ × lagged diff).
* **MA\_Adjustment Calculation**: Formula for error correction.
* **ARIMA\_Prediction Calculation**: AR\_Part + MA\_Adjustment.

To get the actual forecast for `Original[t]`, add `ARIMA_Prediction[t]` to `Original[t-1]`.

---

## 🗅️ Visual Example Using ARIMA(1,1,1)

We simulate a time series with a trend and fit an ARIMA model to forecast the next 10 days:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Generate a sample time series with a trend
np.random.seed(42)
n = 50
time = np.arange(n)
trend = 0.5 * time
noise = np.random.normal(0, 2, n)
series = trend + noise

# Date index
dates = pd.date_range(start='2022-01-01', periods=n, freq='D')
ts = pd.Series(series, index=dates)

# Fit ARIMA(1,1,1)
model = ARIMA(ts, order=(1,1,1))
model_fit = model.fit()

# Forecast next 10 values
forecast = model_fit.forecast(steps=10)

# Plot
plt.figure(figsize=(12, 5))
plt.plot(ts, label='Original Time Series')
plt.plot(forecast.index, forecast, label='Forecast (Next 10 days)', linestyle='--', marker='o')
plt.axvline(ts.index[-1], color='gray', linestyle=':', label='Forecast Start')
plt.title('ARIMA(1,1,1) on Trend+Noise Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()
```

---

## 🧪 Simulated Step-by-Step ARIMA Mechanics

```python
# Generate simple time series with trend + noise
np.random.seed(1)
data = [10]
for t in range(1, 20):
    data.append(data[-1] + np.random.normal(0, 1))

dates = pd.date_range('2022-01-01', periods=len(data), freq='D')
ts = pd.Series(data, index=dates)

# Step 1: Differencing
diff_ts = ts.diff().dropna()

# Step 2: AR(1) prediction using phi
phi = 0.7
ar_pred = diff_ts.shift(1) * phi

# Step 3: MA(1) using previous error
theta = 0.5
errors = diff_ts - ar_pred
ma_adjustment = errors.shift(1) * theta

# Final prediction
final_pred = ar_pred + ma_adjustment

# Combined DataFrame
df = pd.DataFrame({
    'Original': ts,
    'Differenced': diff_ts,
    'AR_Part': ar_pred,
    'MA_Adjustment': ma_adjustment,
    'ARIMA_Prediction': final_pred
})
print(df.head())
```

---

## 🧠 Summary: Layman's Intuition

| Component | Layman Idea                                         |
| --------- | --------------------------------------------------- |
| AR        | "Use past values to guess today."                   |
| I         | "Look at how things are changing, not just values." |
| MA        | "Correct today’s guess using yesterday’s mistake."  |

---

## ❄️ SARIMA: Seasonal ARIMA Explained

SARIMA stands for **Seasonal AutoRegressive Integrated Moving Average**. It extends ARIMA by adding seasonal components to handle patterns that repeat over fixed intervals (like months, quarters, or weeks).

### 🔧 SARIMA(p, d, q)(P, D, Q, s)

| Component   | Meaning                                                                             |
| ----------- | ----------------------------------------------------------------------------------- |
| **p, d, q** | Non-seasonal ARIMA parameters                                                       |
| **P, D, Q** | Seasonal ARIMA parameters                                                           |
| **s**       | Length of the seasonality cycle (e.g., 12 for monthly data with yearly seasonality) |

### 🧠 What SARIMA Does Step-by-Step:

1. **Seasonal Differencing (D)**: Remove repeating seasonal trends.
   $Y'_t = Y_t - Y_{t-s}$

2. **Non-Seasonal Differencing (d)**: Remove non-seasonal trend.

3. **Fit ARIMA** on the doubly-differenced data:

   * AR terms (p): Past values
   * MA terms (q): Past forecast errors
   * Seasonal AR (P): Values from same season in past
   * Seasonal MA (Q): Seasonal error terms

### 🧪 Code Example: SARIMA Forecasting

```python
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Fit SARIMA(p,d,q)(P,D,Q,s)
model = SARIMAX(ts, order=(1,1,1), seasonal_order=(1,1,1,12))
model_fit = model.fit()

# Forecast next 12 periods
forecast = model_fit.forecast(steps=12)

# Plot
plt.figure(figsize=(12, 5))
plt.plot(ts, label='Original Time Series')
plt.plot(forecast.index, forecast, label='SARIMA Forecast', linestyle='--', marker='o')
plt.axvline(ts.index[-1], color='gray', linestyle=':', label='Forecast Start')
plt.title('SARIMA(1,1,1)(1,1,1,12) Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

### 🔄 Summary of SARIMA

| Step                      | Purpose                                  |
| ------------------------- | ---------------------------------------- |
| Seasonal Differencing (D) | Remove repeating patterns (e.g., yearly) |
| Regular Differencing (d)  | Remove trend                             |
| AR and MA Terms           | Learn short-term and seasonal structure  |

Here is a simulated table showing how SARIMA(1,1,1)(1,1,1,4) might work step-by-step (hypothetical example with quarterly seasonality):

| Date    | Original | Seasonal Diff | Differenced | AR\_Part Calculation | AR\_Part | MA\_Adjustment Calculation             | MA\_Adjustment | SARIMA\_Prediction Calculation | SARIMA\_Prediction |
| ------- | -------- | ------------- | ----------- | -------------------- | -------- | -------------------------------------- | -------------- | ------------------------------ | ------------------ |
| 2022-Q1 | 200      | -             | -           | -                    | -        | -                                      | -              | -                              | -                  |
| 2022-Q2 | 220      | -             | -           | -                    | -        | -                                      | -              | -                              | -                  |
| 2022-Q3 | 210      | -             | -           | -                    | -        | -                                      | -              | -                              | -                  |
| 2022-Q4 | 230      | -             | -           | -                    | -        | -                                      | -              | -                              | -                  |
| 2023-Q1 | 260      | 60 (260-200)  | 30          | 0.7 × 30 = 21        | 21       | -                                      | -              | 21 + 0 = 21                    | 21                 |
| 2023-Q2 | 270      | 50 (270-220)  | -10         | 0.7 × 30 = 21        | 21       | 0.5 × (30 - 21) = 4.5                  | 4.5            | 21 + 4.5 = 25.5                | 25.5               |
| 2023-Q3 | 265      | 55 (265-210)  | -5          | 0.7 × -10 = -7       | -7       | 0.5 × (-10 - 21) = -15.5 × 0.5 = -7.75 | -7.75          | -7 + (-7.75) = -14.75          | -14.75             |

* **Seasonal Diff**: Difference from same period last year (e.g., Q1 of 2023 - Q1 of 2022)
* **Differenced**: Remove trend (like ARIMA)
* **AR\_Part**: Past differenced values (non-seasonal)
* **MA\_Adjustment**: Error correction from past non-seasonal errors
* **SARIMA\_Prediction**: Combined prediction

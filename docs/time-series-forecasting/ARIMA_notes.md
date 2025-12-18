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

* **Original**: Raw data values.
* **Differenced**: Change from previous value.
* **AR\_Part**: Forecast using previous differenced value (with weight φ = 0.7).
* **MA\_Adjustment**: Correction using past forecast error (with θ = 0.5).
* **ARIMA\_Prediction**: Final forecast of the differenced value.
* **ARIMA\_Prediction Calculation**: Sum of AR\_Part and MA\_Adjustment.

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

Let me know if you'd like to add SARIMA (seasonal version) or hyperparameter tuning notes!


## Note: (p, q, d) are hyperparameters, $\phi$ and $\theta$ are model parameters


| Term        | Role                       | Set by You?              |
| ----------- | -------------------------- | ------------------------ |
| **p, d, q** | Structural hyperparameters | ✅ Yes (you choose)       |
| **ϕ, θ**    | Model parameters (weights) | ❌ No (learned from data) |


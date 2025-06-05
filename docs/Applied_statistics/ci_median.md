# Confidence Interval (CI) for the Median using Bootstrap

## 📌 Why We Need It
The **median** is a robust measure of central tendency, especially in skewed distributions. However, it does not have a straightforward formula for calculating its confidence interval (unlike the mean). So, we use **bootstrap resampling** to estimate the confidence interval for the median.

---

## 🔢 Step-by-Step Process

1. **Start with your dataset.**
   - Example: `[3, 5, 7, 2, 4, 20, 7]`

2. **Use bootstrap resampling:**
   - Randomly sample with **replacement** from the dataset.
   - Each bootstrap sample should be the **same size** as the original dataset.
   - Repeat this process many times (e.g., **10,000 iterations**).

3. **Calculate the median of each resampled dataset** and store the values.

4. **Sort the list** of all bootstrap medians (optional for plotting).

5. **Compute percentiles**:
   - For a **95% confidence interval**, take the **2.5th percentile** and **97.5th percentile** of the bootstrap medians.

---

## ✅ Correct Python Code

```python
import numpy as np

# Original dataset
original_dataset = [3, 5, 7, 2, 4, 20, 7]

# Set seed for reproducibility
np.random.seed(42)

# Number of bootstrap samples
N = 10000

# Store medians
medians = []

for _ in range(N):
    sample = np.random.choice(original_dataset, size=len(original_dataset), replace=True)
    medians.append(np.median(sample))

# Compute 95% confidence interval
lower, upper = np.percentile(medians, [2.5, 97.5])

print("95% Confidence Interval for the median:", lower, "to", upper)
```

## 🔍 Notes

* The method used here is called the **percentile bootstrap** method.
* You can adjust the confidence level (e.g., use \[5, 95] for a 90% CI).
* Bootstrap is useful when theoretical distributions are unknown or complicated.

---

## 📊 Optional: Plotting the Bootstrap Distribution

```python
import matplotlib.pyplot as plt

plt.hist(medians, bins=50, edgecolor='k')
plt.axvline(lower, color='red', linestyle='--', label=f'2.5% = {lower:.2f}')
plt.axvline(upper, color='red', linestyle='--', label=f'97.5% = {upper:.2f}')
plt.title('Bootstrap Distribution of Median')
plt.xlabel('Median')
plt.ylabel('Frequency')
plt.legend()
plt.show()
```

---

## 🧠 Summary

Bootstrap is a powerful, non-parametric tool to compute confidence intervals for **statistics** that don't have easy closed-form solutions — like the **median**. It's simple to implement and widely used in real-world data science.

## Optional Clarification

* This is called the **percentile bootstrap method** for estimating confidence intervals.

* You can also use **bias-corrected and accelerated (BCa) bootstrap** for improved accuracy, especially when the sampling distribution is skewed.

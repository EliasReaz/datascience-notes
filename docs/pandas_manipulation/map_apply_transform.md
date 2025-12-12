
---

# Pandas Reference: `map()`, `apply()`, `transform()` - with Business Use Cases

## 🗃 Sample Business Dataset

```python
import pandas as pd

df = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Region': ['East', 'West', 'East', 'South', 'West', 'East', 'South', 'West'],
    'PurchaseAmount': [250, 300, 150, 400, 500, 100, 350, 450],
    'LoyaltyLevel': ['Gold', 'Silver', 'Gold', 'Platinum', 'Silver', 'Bronze', 'Gold', 'Silver']
})
```

| CustomerID | Region | PurchaseAmount | LoyaltyLevel |
| ---------- | ------ | -------------- | ------------ |
| 101        | East   | 250            | Gold         |
| 102        | West   | 300            | Silver       |
| 103        | East   | 150            | Gold         |
| 104        | South  | 400            | Platinum     |
| 105        | West   | 500            | Silver       |
| 106        | East   | 100            | Bronze       |
| 107        | South  | 350            | Gold         |
| 108        | West   | 450            | Silver       |

---

## 1️⃣ `map()` - Use for Element-wise Transformation on a **Series**

### 📌 Goal: Map loyalty level to discount rate

```python
discount_map = {'Gold': 0.10, 'Silver': 0.05, 'Platinum': 0.15, 'Bronze': 0.02}
df['DiscountRate'] = df['LoyaltyLevel'].map(discount_map)
```

### 📌 Another Example: Format CustomerID with prefix

```python
df['CustomerTag'] = df['CustomerID'].map(lambda x: f'CUST-{x}')
```

✅ **Use `map()`** when:

* We are transforming values **element-by-element**
* We are working with a **single column (Series)**
* We can use a function or dictionary

---

## 2️⃣ `apply()` - Use for Row/Column-wise Custom Logic

### 📌 Goal: Compute final price after discount (row-wise)

```python
df['FinalAmount'] = df.apply(
    lambda row: row['PurchaseAmount'] * (1 - row['DiscountRate']),
    axis=1
)
```

### 📌 Another Example: Tag high-value customers

```python
df['HighValueTag'] = df.apply(
    lambda row: 'VIP' if row['FinalAmount'] > 300 else 'Regular',
    axis=1
)
```

✅ **Use `apply()`** when:

* We want **access to multiple columns** at once (row-wise logic)
* We need to return **more complex values**
* Be aware: `apply()` can **change the shape**

---

## 3️⃣ `transform()` — Use for Group-wise Computation & Shape Preservation

### 📌 Goal: Normalize purchase amount within each region

```python
df['RegionMean'] = df.groupby('Region')['PurchaseAmount'].transform('mean')
df['NormalizedPurchase'] = df['PurchaseAmount'] / df['RegionMean']
```

### 📌 Another Example: Z-score of purchases within each region

```python
df['Zscore'] = df.groupby('Region')['PurchaseAmount'].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

✅ **Use `transform()`** when:

* You’re doing **group-wise operations**
* You want to **broadcast result back** to each row
* You must **preserve original shape**

---

## ⚖️ Comparison Table

| Feature                      | `map()`           | `apply()`          | `transform()`           |
| ---------------------------- | ----------------- | ------------------ | ----------------------- |
| Works on                     | Series only       | Series / DataFrame | Series / DataFrame      |
| Acts on                      | Individual values | Rows or columns    | Element-wise with shape |
| Can access multiple columns? | ❌ No              | ✅ Yes              | ❌ No                    |
| Keeps original shape         | ✅ Yes             | ❌ Not always       | ✅ Yes                   |
| Great for                    | Clean-up, mapping | Custom row logic   | Group-based engineering |

---

## 🧪 Bonus: Chain all together

```python
# Map loyalty to discount
df['DiscountRate'] = df['LoyaltyLevel'].map(discount_map)

# Format customer ID
df['CustomerTag'] = df['CustomerID'].map(lambda x: f'CUST-{x}')

# Final amount after discount
df['FinalAmount'] = df.apply(
    lambda row: row['PurchaseAmount'] * (1 - row['DiscountRate']),
    axis=1
)

# Region-wise normalization
df['RegionMean'] = df.groupby('Region')['PurchaseAmount'].transform('mean')
df['NormalizedPurchase'] = df['PurchaseAmount'] / df['RegionMean']

# Z-score
df['Zscore'] = df.groupby('Region')['PurchaseAmount'].transform(
    lambda x: (x - x.mean()) / x.std()
)

# High-value tag
df['HighValueTag'] = df.apply(
    lambda row: 'VIP' if row['FinalAmount'] > 300 else 'Regular',
    axis=1
)
```
---

# Add calculated columns based on the combined logic from the markdown example

# Discount mapping
discount_map = {'Gold': 0.10, 'Silver': 0.05, 'Platinum': 0.15, 'Bronze': 0.02}
df_extended['DiscountRate'] = df_extended['LoyaltyLevel'].map(discount_map)

# Customer tag
df_extended['CustomerTag'] = df_extended['CustomerID'].map(lambda x: f'CUST-{x}')

# Final amount after discount
df_extended['FinalAmount'] = df_extended.apply(
    lambda row: row['PurchaseAmount'] * (1 - row['DiscountRate']),
    axis=1
)

# Region-wise mean and normalization
df_extended['RegionMean'] = df_extended.groupby('Region')['PurchaseAmount'].transform('mean')
df_extended['NormalizedPurchase'] = df_extended['PurchaseAmount'] / df_extended['RegionMean']

# Region-wise Z-score
df_extended['Zscore'] = df_extended.groupby('Region')['PurchaseAmount'].transform(
    lambda x: (x - x.mean()) / x.std()
)

# High-value customer tagging
df_extended['HighValueTag'] = df_extended.apply(
    lambda row: 'VIP' if row['FinalAmount'] > 300 else 'Regular',
    axis=1
)

| CustomerID | Region | PurchaseAmount | LoyaltyLevel | DiscountRate | CustomerTag | FinalAmount | RegionMean | NormalizedPurchase | Zscore  | HighValueTag |
| ---------- | ------ | -------------- | ------------ | ------------ | ----------- | ----------- | ---------- | ------------------ | ------- | ------------ |
| 101        | East   | 250            | Gold         | 0.10         | CUST-101    | 225.00      | 166.67     | 1.50               | 1.0911  | Regular      |
| 102        | West   | 300            | Silver       | 0.05         | CUST-102    | 285.00      | 416.67     | 0.72               | -1.1209 | Regular      |
| 103        | East   | 150            | Gold         | 0.10         | CUST-103    | 135.00      | 166.67     | 0.90               | -0.2182 | Regular      |
| 104        | South  | 400            | Platinum     | 0.15         | CUST-104    | 340.00      | 375.00     | 1.07               | 0.7071  | VIP          |
| 105        | West   | 500            | Silver       | 0.05         | CUST-105    | 475.00      | 416.67     | 1.20               | 0.8006  | VIP          |
| 106        | East   | 100            | Bronze       | 0.02         | CUST-106    | 98.00       | 166.67     | 0.60               | -1.3093 | Regular      |
| 107        | South  | 350            | Gold         | 0.10         | CUST-107    | 315.00      | 375.00     | 0.93               | -0.7071 | VIP          |
| 108        | West   | 450            | Silver       | 0.05         | CUST-108    | 427.50      | 416.67     | 1.02               | 0.3203  | VIP          |

---

Absolutely — let’s talk about **why `NormalizedPurchase` is useful** in real-world data work:

---

#### 🎯 What is `NormalizedPurchase`?

This column was created by:

```python
df['NormalizedPurchase'] = df['PurchaseAmount'] / df['RegionMean']
```

It shows how a customer’s purchase compares to the **average purchase amount in their region**.

#### 💡 Why is this useful?

#### ✅ 1. **Contextual Comparison**

A customer who spent \$400:

* May be **above average** in one region
* But **below average** in another

`NormalizedPurchase` allows you to **compare spending behavior relative to regional norms**, instead of using raw numbers.

#### ✅ 2. **Fair Scoring in Regional Campaigns**

If you’re running a **reward campaign**:

* Simply picking "top spenders" may favor high-spending regions (like West)
* Using `NormalizedPurchase` helps pick **outstanding customers** in every region fairly

> Example: A customer with `NormalizedPurchase = 1.5` is spending **50% more than the average customer** in their region.

#### ✅ 3. **Outlier Detection**

Customers with:

* Values ≫ 1 are potential **high-value** or **flagship** customers
* Values ≪ 1 might be **inactive**, or **at-risk** customers

#### ✅ 4. **Feature Engineering for ML**

If you build models (e.g., churn prediction, segmentation), using `NormalizedPurchase`:

* Removes **region bias**
* Helps the model **learn behavior patterns**, not raw differences

#### 🧠 TL;DR

| Raw Purchase | Normalized Purchase | Meaning                  |
| ------------ | ------------------- | ------------------------ |
| \$400        | 1.5                 | 50% above region average |
| \$300        | 0.75                | 25% below region average |
| \$500        | 1.2                 | 20% above region average |

✅ Use `NormalizedPurchase` to **level the playing field**, understand customer behavior, and make region-aware decisions.

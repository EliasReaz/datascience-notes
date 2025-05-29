# 🐼 Pandas Data Transformation Cheat Sheet

## 📘 Example Dataset
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'City': ['Toronto', 'Vancouver', 'Toronto', 'Vancouver'],
    'Temperature': [5, 7, 6, 8],
    'Humidity': [65, 70, 66, 72]
}
df = pd.DataFrame(data)
```

```
         Date      City  Temperature  Humidity
0  2024-01-01   Toronto            5        65
1  2024-01-01  Vancouver           7        70
2  2024-01-02   Toronto            6        66
3  2024-01-02  Vancouver           8        72
```

---

## 1. `pivot_table()`
### ✅ When to use: Aggregating + reshaping data by index/column
### ❓ Question it solves: "What is the average Temperature and Humidity for each City?"
```python
pivot_df = df.pivot_table(index='City', values=['Temperature', 'Humidity'], aggfunc='mean')
```
```
            Humidity  Temperature
City                            
Toronto          65.5         5.5
Vancouver        71.0         7.5
```

---

## 2. `pivot()`
### ✅ When to use: Reshaping without aggregation (must be unique combinations)
### ❓ Question it solves: "How can I see Temperature values by Date and City in a matrix?"
```python
pivot_df = df.pivot(index='Date', columns='City', values='Temperature')
```
```
City         Toronto  Vancouver
Date                          
2024-01-01        5          7
2024-01-02        6          8
```

---

## 3. `groupby()`
### ✅ When to use: Grouping + aggregation without reshaping
### ❓ Question it solves: "What is the average Temperature for each City?"
```python
city_group = df.groupby('City')['Temperature'].mean()
```
```
City
Toronto      5.5
Vancouver    7.5
Name: Temperature, dtype: float64
```

---

## 4. `melt()`
### ✅ When to use: Unpivot a wide table into long format
### ❓ Question it solves: "How can I convert columns (like Temperature, Humidity) into rows for easier plotting or analysis?"
```python
melted = pd.melt(df, id_vars=['Date', 'City'], value_vars=['Temperature', 'Humidity'], 
                 var_name='Measurement', value_name='Value')
```
```
         Date      City Measurement  Value
0  2024-01-01   Toronto  Temperature      5
1  2024-01-01  Vancouver  Temperature      7
2  2024-01-02   Toronto  Temperature      6
3  2024-01-02  Vancouver  Temperature      8
4  2024-01-01   Toronto     Humidity     65
5  2024-01-01  Vancouver     Humidity     70
6  2024-01-02   Toronto     Humidity     66
7  2024-01-02  Vancouver     Humidity     72
```

### 📊 When to use `melt()` for visualization
`melt()` is especially useful for Seaborn or Matplotlib when you want to:
- Plot multiple measurements on the same axes
- Use `hue` for different measurements

```python
sns.lineplot(data=melted, x='Date', y='Value', hue='Measurement')
plt.title('Line Plot of Temperature and Humidity')
plt.show()
```

---

## 5. `stack()`
### ✅ When to use: Convert columns to a row-wise MultiIndex (wide → long)
### ❓ Question it solves: "How can I convert the columns of a pivoted table into row-level entries?"
```python
pivot_df = df.pivot(index='Date', columns='City', values='Temperature')
stacked = pivot_df.stack()  # MultiIndex: Date + City
```
```
Date        City     
2024-01-01  Toronto      5
            Vancouver    7
2024-01-02  Toronto      6
            Vancouver    8
dtype: int64
```

---

## 6. `unstack()`
### ✅ When to use: Convert inner level of row index to column level (long → wide)
### ❓ Question it solves: "How can I reverse the effect of `stack()` and get back the original column layout?"
```python
unstacked = stacked.unstack()  # City becomes columns again
```
```
City         Toronto  Vancouver
Date                          
2024-01-01        5          7
2024-01-02        6          8
```

---

## 🔁 Summary Table
| Function       | Use Case                              | Reshape | Aggregation | Solves What Question?                                | Suitable for Plotting |
|----------------|----------------------------------------|---------|-------------|------------------------------------------------------|------------------------|
| `pivot()`      | Reshape data (must be unique keys)     | ✅      | ❌          | See data matrix across dimensions                   | Wide format            |
| `pivot_table()`| Reshape + aggregate                    | ✅      | ✅          | Average/summarize across categories                 | Wide format            |
| `groupby()`    | Group + aggregate                      | ❌      | ✅          | Summary stats per group                             | Use with aggregation   |
| `melt()`       | Wide → long                            | ✅      | ❌          | Flatten data for analysis/plotting                 | ✅ (long format)        |
| `stack()`      | Columns → row MultiIndex               | ✅      | ❌          | Convert wide to nested long format                 | Not commonly used      |
| `unstack()`    | Row MultiIndex → columns               | ✅      | ❌          | Reverse of stacking                                | Not commonly used      |

---

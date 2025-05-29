# 🧮 pandas Aggregation & Transformation Functions Cheat Sheet

This note covers different pandas aggregation functions (`agg()`, `apply()`, `transform()`) with examples, outputs, and explanations for your MkDocs.

---

## 📥 Sample DataFrame

| group | value1 | value2 | value3 |
| ----- | ------ | ------ | ------ |
| A     | 10     | 100    | 5      |
| A     | 15     | 150    | 3      |
| B     | 10     | 50     | 6      |
| B     | 20     | 60     | 2      |
| C     | 15     | 200    | 7      |
| C     | 30     | 250    | 8      |

---

## 1️⃣ `agg()` - Aggregate with built-in and custom functions

```python
df.agg({
    'value1': ['min', 'max', 'mean'],
    'value2': ['mean', 'std'],
    'value3': lambda x: (x > 4).sum()
})
```

|          | value1 | value2 | value3 |
| -------- | ------ | ------ | ------ |
| min      | 10     |        |        |
| max      | 30     |        |        |
| mean     | 16.67  |        |        |
| mean     |        | 105.83 |        |
| <lambda> |        |        | 4      |

*Explanation:*

* Multiple built-in functions per column.
* Custom lambda counts values > 4 in `value3`.

---

## 2️⃣ `groupby().agg()` - Group-wise aggregation

```python
df.groupby('group').agg({
    'value1': ['mean', 'sum'],
    'value3': lambda x: (x > 5).sum()
})
```

| group | value1 mean | value1 sum | value3 (count >5) |
| ----- | ----------- | ---------- | ----------------- |
| A     | 12.5        | 25         | 0                 |
| B     | 15.0        | 30         | 1                 |
| C     | 22.5        | 45         | 2                 |

*Explanation:*
Aggregation by group with mixed functions.

---

## 3️⃣ `apply()` - Apply any function across DataFrame or group

```python
def range_func(x):
    return x.max() - x.min()

# Apply to entire DataFrame numeric columns
df[['value1', 'value2']].apply(range_func)
```

|   | value1 | value2 |
| - | ------ | ------ |
|   | 20     | 200    |

---

```python
# Apply custom function on groupby object (sum of range per group)
df.groupby('group').apply(lambda g: g[['value1', 'value2']].apply(range_func))
```

| group | value1 | value2 |
| ----- | ------ | ------ |
| A     | 5      | 50     |
| B     | 10     | 10     |
| C     | 15     | 50     |

*Explanation:*

* `apply()` can run any function, returning scalar or DataFrame.
* More flexible but sometimes slower than `agg()`.

---

## 4️⃣ `transform()` - Returns same shape as input, good for feature engineering

```python
# Normalize value1 within each group (subtract mean)
df['value1_norm'] = df.groupby('group')['value1'].transform(lambda x: x - x.mean())
df
```

| group | value1 | value2 | value3 | value1\_norm |
| ----- | ------ | ------ | ------ | ------------ |
| A     | 10     | 100    | 5      | -2.5         |
| A     | 15     | 150    | 3      | 2.5          |
| B     | 10     | 50     | 6      | -5.0         |
| B     | 20     | 60     | 2      | 5.0          |
| C     | 15     | 200    | 7      | -7.5         |
| C     | 30     | 250    | 8      | 7.5          |

*Explanation:*

* `transform()` outputs a result with the same index and shape as original.
* Useful for adding normalized or scaled features.

---

## 5️⃣ Difference between `agg()`, `apply()`, and `transform()`

| Function      | Input Type          | Output Shape                        | Use Case                                      |
| ------------- | ------------------- | ----------------------------------- | --------------------------------------------- |
| `agg()`       | Series or DataFrame | Aggregated scalar(s) or DataFrame   | Summary statistics or aggregation             |
| `apply()`     | Series or DataFrame | Can be scalar, Series, or DataFrame | Flexible function application, complex ops    |
| `transform()` | Series or DataFrame | Same shape as input                 | Element-wise transformations preserving index |

---

# Summary

* Use **`agg()`** for aggregations that reduce data size (e.g., sum, mean).
* Use **`apply()`** for custom, flexible functions that may change shape.
* Use **`transform()`** when you want to return transformed data matching input shape (e.g., normalization).

---

# Bonus: Renaming columns after aggregation

```python
result = df.agg({
    'value1': 'mean',
    'value2': 'sum'
})

result.rename({
    'value1': 'Avg Value1',
    'value2': 'Total Value2'
}, inplace=True)

print(result)
```

| Avg Value1 | Total Value2 |
| ---------- | ------------ |
| 16.67      | 810          |

---

*Happy coding with pandas!* 🚀

```

---

If you want, I can prepare a downloadable `.md` file for you to upload?
```

# 📉 Pandas `melt()` Explained (Wide to Long Format)

The `pandas.melt()` function is used to reshape a dataframe from **wide** format to **long** format. This is useful when you want to gather multiple columns into key-value pairs for easier analysis or visualization.

---

## 🧪 Example Use Case

Suppose you have a dataframe named `df_main` with the shape `(2, 4)` and columns like:

* Before melting:

| SAM | Year | Species31 | Species61 |
| --- | ---- | --------- | --------- |
| A   | 2021 | 10        | 5         |
| B   | 2021 | 0         | 3         |

```python
df_long = pd.melt(
    df_wide,
    id_vars=['SAM', 'Year'], # cols to keep fixed
    value_vars=['Species31', 'Species61'], # cols names from old df_wide we like to melt
    var_name='Species', # name of new colum 
    value_name='Catches' # name of new column that stores the value from those melted
)
```

* After melting:

| SAM | Year | Species   | Catch |
| --- | ---- | --------- | ----- |
| A   | 2021 | Species31 | 10    |
| B   | 2021 | Species31 | 0     |
| A   | 2021 | Species61 | 5     |
| B   | 2021 | Species61 | 3     |

---



### parameter breakdown of `pd.melt(df_to_be_melted, id_vars, value_vars, var_name, value_name)`

| Parameter    | Description                                                                                |
| ------------ | ------------------------------------------------------------------------------------------ |
| `id_vars`    | Columns to keep fixed (e.g., metadata like `SAM`, `Year`, etc.)                            |
| `value_vars` | The **column names** you want to melt (e.g., `Species31`, `Species61`, ...)                |
| `var_name`   | Name for the new column that stores the melted column names (e.g., `'Species'`)            |
| `value_name` | Name for the new column that stores the values from those melted columns (e.g., `'Catch'`) |

---

### Summary

Use `melt()` to convert wide data (many similar columns) into long format (fewer columns, more rows).

* Great for tidy data, easier filtering, plotting, or exporting.

* Keep identifier columns with id_vars.

* Collapse similar columns with value_vars.

* Control output names with `var_name` and `value_name`.

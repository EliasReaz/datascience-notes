## 📝 Data Science Test Preparation

### Part I: Data Analysis & Cleaning (Exploratory Phase)

This part focuses on initial data quality assessment, cleaning sparse/inconsistent data, and early discovery of usage patterns.

#### 1\. Data Inspection & Missing Data

  * **Function:** `df.info()` to check data types and count non-null values.
  * **Function:** `df.isnull().sum()` to quickly count missing (null) values per column.
  * **Action on Sparsity:** Used **`df.dropna(axis=1, thresh=N)`** (where $N$ is the required minimum of non-null values) to drop columns that were too sparse (e.g., threshold set to 20 for 100 rows).

## 🗑️ Pandas `df.dropna()` Actions

| Drop Action | Code | Rule |
| :--- | :--- | :--- |
| **Drop Sparse Columns** | `df.dropna(axis=1, thresh=N)` | **Keep** a column only if it has at least **N** non-null values (applied across the rows). |
| **Drop Rows (Default)** | `df.dropna(axis=0)` or `how='any'` | Drop the **entire row** if **any** value in that row is null. |
| **Drop Empty Rows** | `df.dropna(axis=0, how='all')` | Drop the **entire row** only if **all** values in that row are null. |
| **Drop Rows (Specific Thresh)** | `df.dropna(axis=0, thresh=N)` | **Keep** a row only if it has at least **N** non-null values (applied across the columns). |


#### 2\. Handling Inconsistent Text Data

  * **Action:** Standardizing text features (like `'country'`) to a uniform case.
      * **Code:** `df['country'] = df['country'].str.lower()`
  * **Action:** Removing inconsistent characters (spaces, periods) using string replacement.
      * **Function:** **`df.str.replace(pattern, replacement, regex=False)`**
      * **Key Guardrail:** Always use `regex=False` when replacing literal characters (like `.` or `     `) to prevent accidental deletion of entire strings due to regex wildcard matching.

#### 3\. Handling Inconsistent Date/Time Data

  * **Function:** **`pd.to_datetime()`** is the essential function for converting object/string columns to `datetime64`.
  * **Action on Mixed Formats:** For columns with multiple date string formats (e.g., `'15-Jan-2025'` and `'01/15/2025'`), use the `infer_datetime_format=True` argument to allow Pandas to guess the format for each entry, ensuring successful conversion.

#### 4\. Numerical Analysis & Outlier Detection

  * **Function:** **`df.describe()`** provides the essential summary statistics (mean, min, max, $Q_1$, $Q_2$, $Q_3$) for numerical data.
  * **Outlier Method:** The **IQR (Interquartile Range) method** is the most robust technique for skewed usage data.
      * **Key Concept:** The **Median ($Q_2$)** is the best measure of a "typical" user session for right-skewed data because it is not inflated by extreme outliers (unlike the mean).
  * **Visualization:** Use **`sns.boxplot(data=df['column'])`** to visually confirm IQR outliers.

#### 5\. Categorical Analysis & Visualization

  * **Function:** **`df['column'].value_counts()`** returns the count (frequency) of unique values.
  * **Function for Percentage:** Use **`df['column'].value_counts(normalize=True)`** to get the relative frequency (proportion).
  * **Visualization (Frequency):** Use **`df['column'].value_counts().plot(kind='bar')`** for a quick frequency bar chart.
  * **Visualization (Comparison):** Use the **`hue`** argument in Seaborn (`sns.countplot` or `sns.boxplot`) to compare distributions or counts across a third variable (e.g., `sns.boxplot(x=..., y=..., hue='Region')`).

#### 6\. Relationship Analysis

  * **Function:** **`df.corr()`** generates the correlation matrix for all numerical pairs.
  * **Visualization:** **`sns.heatmap(df.corr(), annot=True)`** is used to visually represent the correlation matrix, with `annot=True` displaying the numerical correlation coefficients.
  * **Key Concept:** Strong correlation (multicollinearity) means features are redundant; the recommendation is to **drop one** or create a **composite feature**.

-----

### Part II: Data Wrangling & Reporting (Transformation Phase)

This part focuses on efficiently transforming data into custom, structured reports based on specific business criteria.

#### 1\. Filtering & Subsetting

  * **Technique:** **Boolean Indexing (Masking)**.
  * **Code:** `df[ (df['condition_A']) & (df['condition_B']) ]` using parentheses for each condition and `&` (AND) or `|` (OR) operators.

#### 2\. Advanced Aggregation for Custom Reports

  * **Function:** **`df.groupby().agg()`** is used to apply multiple aggregation functions to multiple columns.
  * **Code Structure:** Use a **dictionary** within `agg()` to specify functions per column:
    ```python
    df.groupby('Device').agg({
        'session_duration': ['mean', 'median'],  # Multiple functions for one column
        'user_id': 'nunique'                    # Different function for a second column
    })
    ```

#### 3\. Restructuring for Wide Reports

  * **Function:** **`pd.pivot_table()`** is used to transform data from a long format to a wide summary table.
  * **Code Structure:** Requires defining the three key components:
    ```python
    pd.pivot_table(
        data=df,
        index='Region',      # New ROWS
        columns='Device_Type', # New COLUMN HEADERS
        values='Duration',   # Data in the cells
        aggfunc='mean'       # Aggregation (default is mean)
    )
    ```

#### 4\. Communication Strategy (The Email)

  * **Three Key Findings:** Prioritize the three most critical findings for the email:
    1.  **Missing Data (Sparsity):** Which columns are $>80\%$ null? **Caution:** Statistics from these columns are **not representative**.
    2.  **Usage Profile (Skew/Outliers):** Report the **Median** session duration as the reliable center, noting the mean is inflated by outliers.
    3.  **Correlation/Redundancy:** Report any strong correlations (e.g., $r=0.85$) and recommend **dropping one feature** or creating a **composite feature** for future modeling.

-----

This summary covers every major technical detail and communication point from our preparation.
# 📚 Advanced SQL Reference Guide: Core Concepts

## 1\. 🤝 Pattern: Self-Join for Unique Pair Counting

**🎯 Goal:** Find and count unique relationships between entities in the same table (e.g., lawyers sharing a trial).

**🔑 Key Logic: Eliminating Duplicate Pairs**
Joining a table to itself (`T1` to `T2`) requires a condition to prevent double-counting of pairs (e.g., counting A/B and B/A).

  - **`T1.id < T2.id`**: The most common and effective way to ensure only one order is counted.

**💻 SQL Code Template:**

```sql
SELECT
    T1.lawyer_id AS Lawyer_A,
    T2.lawyer_id AS Lawyer_B,
    COUNT(T1.trial_id) AS Shared_Count
FROM
    TrialParticipation AS T1
JOIN
    TrialParticipation AS T2
    ON T1.trial_id = T2.trial_id   
    AND T1.lawyer_id < T2.lawyer_id -- CRITICAL: Eliminate duplicates
GROUP BY
    Lawyer_A, Lawyer_B;
```

-----

## 2\. 🗓️ Pattern: Streak Finding (`ROW_NUMBER()`)

**🎯 Goal:** Find the longest continuous sequence (streak) of dates or events.

**🔑 Key Logic: The Group ID Trick**
Use `ROW_NUMBER()` to assign a sequential integer to every successful row. Subtracting this integer from the date creates a `Group ID` that stays constant only during a continuous streak.

**💻 SQL Code Template (PostgreSQL):**

```sql
WITH tbl_high_sales AS (
    SELECT sale_date FROM DailySales WHERE sales_amount > 1000
),
tbl_streaks_grouped AS (
    SELECT 
        sale_date, 
        -- Creates a unique ID for each continuous streak
        sale_date - (ROW_NUMBER() OVER (ORDER BY sale_date) * INTERVAL '1 day') AS streak_group_id
    FROM tbl_high_sales
)
SELECT 
    MIN(sale_date) AS Start_Date,
    MAX(sale_date) AS End_Date,
    COUNT(sale_date) AS Streak_Length 
FROM tbl_streaks_grouped
GROUP BY streak_group_id;
```

-----

## 3\. 📈 Pattern: Time Series Comparison (`LAG()`)

**🎯 Goal:** Calculate Month-Over-Month (MOM) percentage change.

**🔑 Key Logic: `LAG()` and Safe Casting**

  - `LAG()` brings a value from a previous row into the current row for easy comparison.
  - **`CAST(... AS NUMERIC)`**: Essential to prevent **integer division** (which truncates the result to 0) when calculating percentages.

**💻 SQL Code Template:**

```sql
WITH tbl_monthly_sales AS (
    SELECT DATE_TRUNC('month', sale_date) AS sale_month, SUM(sales_amount) AS total_sales
    FROM DailySales GROUP BY sale_month
),
tbl_lagged_sales AS (
    SELECT 
        total_sales,
        LAG(total_sales, 1) OVER(ORDER BY sale_month ASC) AS prev_month_sales 
    FROM tbl_monthly_sales
)
SELECT 
    CAST((total_sales - prev_month_sales) AS NUMERIC) / prev_month_sales AS mom_percent_change
FROM tbl_lagged_sales;
```

-----

## 4\. ⚙️ SQL Execution Order and Filtering Clauses

The order in which these clauses are written determines when the filtering happens.

| Clause | Purpose | Execution Order | Can use Aggregation? |
| :---: | :---: | :---: | :---: |
| **`WHERE`** | Filters **Individual Rows**. | 2nd (Before Grouping) | 🚫 **No.** Filters raw data. |
| `GROUP BY` | Aggregates remaining rows. | 3rd | |
| **`HAVING`** | Filters **Groups/Totals**. | 4th (After Grouping) | ✅ **Yes.** Filters based on `SUM()`, `COUNT()`, etc. |
| `ORDER BY` | Sorts final results. | 6th (Last) | ✅ **Yes.** |

**Practical Example:**

```sql
SELECT product_category, SUM(amount) AS total_sales
FROM SalesTransactions
WHERE EXTRACT(YEAR FROM transaction_date) = 2025 -- 1. WHERE: Filter sales in 2025
  AND amount > 100                               -- 1. WHERE: Filter individual transactions > 100
GROUP BY product_category
HAVING SUM(amount) > 50000;                      -- 2. HAVING: Filter categories with total sales > 50k
```

-----

## 5\. 📅 PostgreSQL Date Function Comparison

Both functions are used to filter dates, but they return different data types, which affects how you write your comparisons.

| Function | Output Data Type | Comparison Example | Use Case |
| :---: | :---: | :---: | :---: |
| **`EXTRACT(YEAR FROM date)`** | **Integer** (e.g., 2025) | `WHERE EXTRACT(YEAR FROM date) = 2025` | Simple comparison against a specific numerical part of the date (year, month, day). |
| **`DATE_TRUNC('unit', date)`** | **Timestamp** (e.g., `2025-01-01 00:00:00`) | `WHERE DATE_TRUNC('year', date) = '2025-01-01'` | Used for grouping time periods (like `GROUP BY DATE_TRUNC('month', date)`) or filtering ranges. |

-----

You've built a strong knowledge base\! Since you've mastered filtering, aggregation, and time series, what would you like to explore next?

1.  **🌲 Recursive CTEs:** Learning to query hierarchical data (like finding all managers in a management chain).
2.  **🔍 SQL Performance Tuning:** Discussion of indexing and optimization for queries.
3.  **🪟 Other Window Functions:** Exploring `LEAD()` and using partitions (`PARTITION BY`).
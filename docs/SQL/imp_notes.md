# 💾 Advanced SQL Patterns: Comprehensive Reference

This guide summarizes four advanced SQL techniques: Self-Joins for pairing, Window Functions for streak analysis (`ROW_NUMBER()`), time-series comparison (`LAG()`), and the difference between ranking functions.

## 1. 🤝 Pattern: Self-Join for Unique Pair Counting

**🎯 Goal:** Find and count unique relationships between entities in the same table (e.g., lawyers sharing a trial).

**🏷️ Table Schema:**
| Table | Column | Type |
| :---: | :---: | :---: |
| `TrialParticipation` | `trial_id` | INT |
| | `lawyer_id` | INT |

**🔑 Key Logic: Eliminating Duplicate Pairs**
Joining a table to itself creates redundant pairs (A, B and B, A). The condition below ensures only one is counted:
- **`T1.lawyer_id < T2.lawyer_id`**: Forces the lawyer with the lower ID to always be listed first.

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
    AND T1.lawyer_id < T2.lawyer_id -- CRITICAL: Eliminates duplicates
GROUP BY
    Lawyer_A, Lawyer_B
ORDER BY
    Shared_Count DESC;
````

-----

## 2\. 🗓️ Pattern: Streak Finding (`ROW_NUMBER()`)

**🎯 Goal:** Find the longest continuous sequence of successful days (sales \> $1000).

**🏷️ Table Schema:**
| Table | Column | Type |
| :---: | :---: | :---: |
| `DailySales` | `sale_date` | DATE |
| | `sales_amount` | INT |

**🔑 Key Logic: The Group ID Trick**
The difference between the date and the row number is **constant** during a streak but **changes** when a date gap occurs.
$$\text{Group ID} = \text{Sale Date} - \text{ROW\_NUMBER}()$$

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
FROM 
    tbl_streaks_grouped
GROUP BY 
    streak_group_id
ORDER BY 
    Streak_Length DESC
LIMIT 1;
```

-----

## 3\. 📈 Pattern: Time Series Comparison (`LAG()`)

**🎯 Goal:** Calculate the Month-Over-Month (MOM) percentage change in sales.

**🔑 Key Logic: The `LAG()` Function & Type Casting**

  - `LAG(value, 1) OVER (ORDER BY time)`: Efficiently brings the previous row's value into the current row.
  - **`CAST` to NUMERIC**: Required to prevent **integer division** (which truncates decimals) when calculating the percentage change.

**💻 SQL Code Template (PostgreSQL):**

```sql
WITH tbl_monthly_sales AS (
    SELECT  
        DATE_TRUNC('month', sale_date) AS sale_month,
        SUM(sales_amount) AS total_sales
    FROM DailySales
    GROUP BY sale_month
),
tbl_lagged_sales AS (
    SELECT 
        sale_month, 
        total_sales,
        LAG(total_sales, 1) OVER(ORDER BY sale_month ASC) AS prev_month_sales 
    FROM tbl_monthly_sales
)
SELECT 
    sale_month, 
    total_sales, 
    prev_month_sales,
    -- Forces floating-point division for accurate percentage
    CAST((total_sales - prev_month_sales) AS NUMERIC) / prev_month_sales AS mom_percent_change
FROM tbl_lagged_sales;
```

-----

## 4\. 🔢 Window Function: Ranking (`RANK` vs. `DENSE_RANK`)

**🎯 Goal:** Assign ranks based on value, differentiating how ties are handled.

| Function | Tie Handling | Rank Jumps? | Example (100, 100, 90, 80) |
| :--- | :--- | :--- | :--- |
| **`RANK()`** | Same rank for ties. | **Yes.** | 1, 1, **3**, 4 |
| **`DENSE_RANK()`** | Same rank for ties. | **No.** | 1, 1, **2**, 3 |

**💻 SQL Code Template (`DENSE_RANK` Example):**

```sql
SELECT 
    student_name,
    exam_score,
    -- Used to find the 'top N distinct score tiers'
    DENSE_RANK() OVER (ORDER BY exam_score DESC) AS score_rank
FROM 
    StudentScores
WHERE
    DENSE_RANK() OVER (ORDER BY exam_score DESC) <= 2;
```


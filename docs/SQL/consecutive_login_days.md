Absolutely! Let’s expand the markdown with a detailed example involving **3 users**: `1032`, `1050`, and `1002`. This will help you clearly see how the `streak_marker`, `streak_id`, and final output work.

Here’s the updated and elaborated markdown example:

---

````markdown
# SQL Walkthrough: Finding Users with 10+ Consecutive Login Days

This walkthrough explains how to identify users who have logged in for **at least 10 consecutive days**, using SQL Common Table Expressions (CTEs). We show the process **step-by-step**, using a sample dataset for 3 users: `1032`, `1050`, and `1002`.

---

## 🧾 Table Structure

We start with the following table:

```sql
user_login(
  user_id INT,
  login_date DATE
)
````

---

## 👥 Sample Data for 3 Users

| user\_id | login\_date |
| -------- | ----------- |
| 1032     | 2019-01-01  |
| 1032     | 2019-01-02  |
| 1032     | 2019-01-03  |
| 1032     | 2019-01-04  |
| 1032     | 2019-01-05  |
| 1032     | 2019-01-06  |
| 1032     | 2019-01-07  |
| 1032     | 2019-01-08  |
| 1032     | 2019-01-09  |
| 1032     | 2019-01-10  |
| 1032     | 2019-01-11  |
| 1032     | 2019-01-13  |
| 1050     | 2020-02-10  |
| 1050     | 2020-02-11  |
| 1050     | 2020-02-12  |
| 1050     | 2020-02-13  |
| 1050     | 2020-02-14  |
| 1050     | 2020-02-15  |
| 1050     | 2020-02-16  |
| 1050     | 2020-02-17  |
| 1050     | 2020-02-18  |
| 1050     | 2020-02-19  |
| 1002     | 2021-05-01  |
| 1002     | 2021-05-03  |
| 1002     | 2021-05-04  |
| 1002     | 2021-05-06  |

---

## Step 1️⃣: Add Previous Login Date

```sql
WITH my_prior_login_dates AS (
  SELECT
    user_id,
    login_date,
    LAG(login_date) OVER(PARTITION BY user_id ORDER BY login_date) AS prior_login_date
  FROM user_login
)
```

### 🔍 Output (simplified)

| user\_id | login\_date | prior\_login\_date |
| -------- | ----------- | ------------------ |
| 1032     | 2019-01-01  | (null)             |
| 1032     | 2019-01-02  | 2019-01-01         |
| ...      | ...         | ...                |
| 1050     | 2020-02-10  | (null)             |
| 1050     | 2020-02-11  | 2020-02-10         |
| ...      | ...         | ...                |
| 1002     | 2021-05-01  | (null)             |
| 1002     | 2021-05-03  | 2021-05-01         |
| ...      | ...         | ...                |

---

## Step 2️⃣: Mark Streak Breaks

```sql
, my_marker AS (
  SELECT
    *,
    CASE 
      WHEN DATE_PART('day', login_date - prior_login_date) = 1 
           OR prior_login_date IS NULL THEN 0
      ELSE 1
    END AS streak_marker
  FROM my_prior_login_dates
)
```

### 🔍 Output

| user\_id | login\_date | prior\_login\_date | streak\_marker |
| -------- | ----------- | ------------------ | -------------- |
| 1032     | 2019-01-01  | (null)             | 0              |
| 1032     | 2019-01-02  | 2019-01-01         | 0              |
| 1032     | 2019-01-03  | 2019-01-02         | 0              |
| ...      | ...         | ...                | ...            |
| 1032     | 2019-01-13  | 2019-01-11         | 1              |
| 1050     | 2020-02-10  | (null)             | 0              |
| 1050     | 2020-02-11  | 2020-02-10         | 0              |
| ...      | ...         | ...                | ...            |
| 1002     | 2021-05-01  | (null)             | 0              |
| 1002     | 2021-05-03  | 2021-05-01         | 1              |
| 1002     | 2021-05-04  | 2021-05-03         | 0              |
| 1002     | 2021-05-06  | 2021-05-04         | 1              |

---

## Step 3️⃣: Assign Streak ID

```sql
, my_streaks AS (
  SELECT
    user_id,
    login_date,
    SUM(streak_marker) OVER (PARTITION BY user_id ORDER BY login_date) AS streak_id
  FROM my_marker
)
```

### 🔍 Output

| user\_id | login\_date | streak\_id |
| -------- | ----------- | ---------- |
| 1032     | 2019-01-01  | 0          |
| 1032     | 2019-01-02  | 0          |
| 1032     | 2019-01-03  | 0          |
| ...      | ...         | ...        |
| 1032     | 2019-01-13  | 1          |
| 1050     | 2020-02-10  | 0          |
| 1050     | 2020-02-11  | 0          |
| ...      | ...         | ...        |
| 1002     | 2021-05-01  | 0          |
| 1002     | 2021-05-03  | 1          |
| 1002     | 2021-05-04  | 1          |
| 1002     | 2021-05-06  | 2          |

* Each `streak_id` represents a separate run of consecutive login days.

---

## Step 4️⃣: Filter 10+ Day Streaks

```sql
SELECT 
  user_id, 
  MIN(login_date) AS first_login_date, 
  COUNT(*) AS consecutive_login_days
FROM my_streaks
GROUP BY user_id, streak_id
HAVING COUNT(*) >= 10;
```

### ✅ Final Output

| user\_id | first\_login\_date | consecutive\_login\_days |
| -------- | ------------------ | ------------------------ |
| 1032     | 2019-01-01         | 11                       |
| 1050     | 2020-02-10         | 10                       |

### ⚠️ Why 1002 is not in result:

User `1002` never had 10 consecutive login days. Their logins were non-consecutive or had short streaks:

* 2021-05-01 → gap → 2021-05-03 → 2021-05-04 → gap → 2021-05-06

---

## ✅ Summary

| Concept                 | Description                                     |
| ----------------------- | ----------------------------------------------- |
| `LAG()`                 | Finds prior login for each user                 |
| `streak_marker`         | 1 if gap occurred, 0 if login is consecutive    |
| `streak_id`             | Increases when a new streak starts              |
| `GROUP BY`              | Each `(user_id, streak_id)` group is one streak |
| `HAVING COUNT(*) >= 10` | Filters only those streaks with 10 or more days |

This method allows you to **track multiple streaks per user**, and analyze login behavior in a clean, scalable way.

---

# 📊 SQL: GroupBy Monthly Customer Stats

## 🔍 Objective

Get the total number of customers per month and average sales per customer per month.

---

## 🧱 Sample Table Structure

Assume we have a table called `sales_data`:

| Column         | Data Type    | Description                          |
|----------------|--------------|--------------------------------------|
| sale_id        | INT          | Unique identifier for the sale       |
| customer_id    | INT          | Customer making the purchase         |
| sale_amount    | DECIMAL      | Total amount of the sale             |
| sale_date      | DATE         | Date when the sale occurred          |

---

## 📌 SQL Query

```sql
SELECT
  DATE_FORMAT(sale_date, '%Y-%m') AS sale_month,
  COUNT(DISTINCT customer_id) AS total_customers,
  SUM(sale_amount) / COUNT(DISTINCT customer_id) AS avg_sales_per_customer
FROM
  sales_data
GROUP BY
  DATE_FORMAT(sale_date, '%Y-%m')
ORDER BY
  sale_month;
```

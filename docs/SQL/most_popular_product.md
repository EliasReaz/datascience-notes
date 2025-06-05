# 📦 SQL Question: Most Popular Product on Instagram Shop


### 📝 Requirements:

You are working for **Instagram Shop**, and your team wants to know what is the **most popular product**. Write a SQL query to find **1 product** with the **highest number of orders**. In case of a **tie** in order counts, select the product that comes **first in alphabetical order**.

---

### 📊 Tables

#### `orders` table

| Column Name  | Description                      |
| ------------ | -------------------------------- |
| id           | Unique identifier for each order |
| product\_id  | Identifier for the product       |
| customer\_id | Identifier for the customer      |
| order\_date  | Date the order was placed        |

#### `products` table:

| Column Name  | Description                        |
| ------------ | ---------------------------------- |
| id           | Unique identifier for each product |
| name         | Name of the product                |
| price        | Price of the product               |
| category\_id | Identifier for the category        |

---

### ✅ SQL Answer:

```sql
WITH tbl_PRODUCT_COUNT AS (
  SELECT 
    P.name AS product_name, 
    COUNT(O.product_id) AS order_counts
  FROM orders O 
  JOIN products P ON O.product_id = P.id
  GROUP BY P.name
)
SELECT product_name
FROM tbl_PRODUCT_COUNT
ORDER BY order_counts DESC, product_name ASC
LIMIT 1;
```

---

### 💡 Explanation:

* `JOIN` combines order and product info.
* `COUNT(O.product_id)` counts how many times each product was ordered.
* `GROUP BY P.name` groups orders by product.
* `ORDER BY order_counts DESC, product_name ASC` ensures:

  * Most popular product comes first.
  * Alphabetical order is used to break ties.
* `LIMIT 1` returns just the top product.

---

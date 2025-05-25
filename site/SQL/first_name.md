## SQL Task

**Goal**: Return a single string like `2, Alan, Adam` for all student names that start with 'A' or 'a', using the `students` table.

**Table: `students`**

| Column Name | Description               |
|-------------|---------------------------|
| first_name  | The first name of student |

---

## ✅ PostgreSQL Query

```sql
SELECT 
    COUNT(*) || ', ' || STRING_AGG(first_name, ', ') AS result
FROM students
WHERE first_name ILIKE 'a%';
```

### Explanation:

- `ILIKE 'a%'`: case-insensitive match for names starting with 'a' or 'A'
- `STRING_AGG(...)`: concatenates the names with a comma and a space
- `COUNT(*) || ', ' || ...`: formats the output as a single string

---

## ✅ MySQL Query (8.0+)

```sql
SELECT 
    CONCAT(COUNT(*), ', ', GROUP_CONCAT(first_name SEPARATOR ', ')) AS result
FROM students
WHERE LOWER(first_name) LIKE 'a%';
```

### Explanation:
- `LOWER(first_name) LIKE 'a%'`: ensures case-insensitive matching
- `GROUP_CONCAT(...)`: joins names with a comma and a space
- `CONCAT(...)`: formats the final output

---

## Output in a tablular form

```sql
SELECT 
    COUNT(*) AS name_count,
    STRING_AGG(first_name, ', ') AS names
FROM students
WHERE first_name ILIKE 'a%';
```

If the table has different first name like:

|first_name|
|-----------|
|Alan|
|adam|
|Bob|
|Annie|

The output will be

|name_count|names|
|---|---|
|3|Alan, adam, Annie| 

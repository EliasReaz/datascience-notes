# Best Paid Job Titles

SELECT the job titles of the highest-paid employees.Your output should list the job title or titles with the highest salary, considering the possibility of multiple titles sharing the same salary.

worker table:

|Field   | Description|
|---     |---         |
| worker_id |Identifier of worker|
|first_name |First name of worker|
|last_name| Last name of worker|
|salary|Salary of worker|
|joining_date| Date of joining|
|department |Department name|


title table:

|Field| Description|
|---|--- |
|title_id | ID of the title|
|worker_ref_id| Identifier of worker|
|worker_title| Name of the position|
|affected_from| Date of modification|

```sql
with tbl_join_worker_title AS
(SELECT W.WORKER_ID, W.SALARY, T.WORKER_TITLE,
DENSE_RANK() OVER(ORDER BY W.SALARY desc) AS RNK
FROM WORKER AS W 
INNER JOIN TITLE T ON W.WORKER_ID = T.WORKER_REF_ID
)
SELECT WORKER_TITLE AS BEST_PAID_TITLE
FROM tbl_join_worker_title 
WHERE RNK=1 
```

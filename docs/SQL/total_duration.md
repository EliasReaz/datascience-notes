# Calculate Total Active Hours for Each User

Calculate the total active hours for each user. You should use the start and end times of user sessions, defined by the session state: '1' for session start and '0' for session end.

user_sessions table:

|Column Name | Description|
|--- |---|
|customer_id| Customer's unique identifier|
|state| Session's state (1 for start, 0 for end)|
|timestamp| Timestamp of the session state|


|customer_id| state | timestamp |
|--- |--- |--- |
|c001| 1 | 07:00:00 |
|c001| 0 | 09:30:00 |
|c001| 1 | 12:00:00 |

---

Example Output:

|customer_id|total_hours|
|--- |---|
|c005|19|

---

```sql
WITH tbl_start_state AS 
(SELECT customer_id, state AS start_state, timestamp AS start_time,
ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY timestamp) AS rn
from user_sessions
where state = 1
),

tbl_end_state AS (Select customer_id, state AS end_state, 
timestamp AS end_time,
ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY timestamp) AS rn
from user_sessions
where state = 0
),

tbl_combine AS (SELECT s.customer_id, 
s.start_state, e.end_state, s.start_time, e.end_time
FROM tbl_start_state s JOIN tbl_end_state e 
ON s.customer_id = e.customer_id AND s.rn=e.rn), 

tbl_duration AS(
select customer_id, start_state, end_state, 
start_time, end_time, 
EXTRACT(EPOCH FROM (end_time-start_time))/3600.0 AS hr_duration from tbl_combine)

SELECT customer_id, SUM(hr_duration) AS total_hours
FROM tbl_duration
GROUP BY customer_id
```

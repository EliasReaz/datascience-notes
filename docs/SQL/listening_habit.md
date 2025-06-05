# 🎧 SQL Challenge: Analyze Spotify-like Listening Habits

## 📘 Question

You're assigned to analyze a **Spotify-like dataset** that records user listening habits.

---

## 📝 Task

For **each user**, compute:

- ✅ The total listening time (in **minutes**), rounded to the **nearest whole number**
- ✅ The number of **unique songs** they've listened to

---

## 🗃️ Table: `listening_habits`

| Column Name      | Description                        |
|------------------|------------------------------------|
| `user_id`        | Identifier of user                 |
| `song_id`        | Identifier of song                 |
| `listen_duration`| Listening time (in seconds)        |

---

## 📌 Expected Output

| user_id | total_listen_duration | unique_song_count |
|---------|------------------------|--------------------|
| 101     | 8                      | 2                  |
| 102     | 5                      | 2                  |

---

## ✅ SQL Answer

```sql
SELECT 
  user_id, 
  ROUND(SUM(listen_duration) / 60.0) AS total_listen_duration, 
  COUNT(DISTINCT song_id) AS unique_song_count
FROM listening_habits
GROUP BY user_id;
```

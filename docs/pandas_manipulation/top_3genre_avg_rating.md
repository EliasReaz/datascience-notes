# Top 3 Actors by Genre Average Rating

Identify the top 3 actors with the highest average movie ratings within their most frequent (i.e., top) genre. For each actor, return their name, top genre, and average rating in that genre.

Conditions:
* If an actor has multiple top genres (same number of appearances), choose the one with the highest average rating.
* If multiple actors share the same average rating (i.e., a tie in rank), include all tied actors, even if this results in more than 3 total actors. Do not skip rank: if all tied actors share the same rank, the next rank follows sequentially.

DataFrame: top_actors_rating
actor_name: object
genre: object
movie_rating: float64
movie_title: object
release_date: datetime64[ns]
production_company: object

|actor_name|genre|movie_rating|movie_title|release_date|production_company|
|--- |--- |--- |---  |---  |---  |
|Ryan Gosling|drama|9|Urban Hunt|2017-07-03|Google|
|Ryan Gosling|sci-fi|8.9|Veil of Secrets| 2015-12-23| Apple|
|Chris Evans|drama|6.1|Crimson Chase|2017-08-10|Apple|

---

### 🎬 Sample Data: `top_actors_rating`

| actor_name        | genre    | movie_rating | movie_title | release_date | production_company |
|-------------------|----------|---------------|--------------|---------------|---------------------|
| Tom Hanks         | Drama    | 8.5           | Movie A      | 2000-01-01    | Studio 1            |
| Tom Hanks         | Comedy   | 7.0           | Movie B      | 2002-01-01    | Studio 1            |
| Emma Stone        | Comedy   | 9.0           | Movie C      | 2010-01-01    | Studio 2            |
| Emma Stone        | Romance  | 8.8           | Movie D      | 2011-01-01    | Studio 2            |
| Denzel Washington | Thriller | 8.8           | Movie E      | 2005-01-01    | Studio 3            |

---

```python
import pandas as pd

# group by actor and genre. because if an actor has multiple genre, we take one with highest average rating

groupby_actor_genre = top_actors_ratings.groupby(['actor_name', 'genre']).agg(count_genre=('genre':'count'), avg_rating=('movie_rating':'mean')).reset_index()
```

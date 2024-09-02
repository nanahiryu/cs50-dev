SELECT DISTINCT(movies.title)
FROM movies
INNER JOIN ratings
ON ratings.movie_id = movies.id
INNER JOIN stars
ON stars.movie_id = movies.id
INNER JOIN people
ON people.id = stars.person_id
ORDER BY ratings.rating DESC
LIMIT 5;
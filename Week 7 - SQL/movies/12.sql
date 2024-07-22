-- List the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred
SELECT title
FROM movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON people.id = stars.person_id
WHERE name = 'Bradley Cooper'
AND title IN
(
    SELECT title
    FROM movies
    JOIN stars ON stars.movie_id = movies.id
    JOIN people ON people.id = stars.person_id
    WHERE name = 'Jennifer Lawrence'
)
ORDER BY movie_id;

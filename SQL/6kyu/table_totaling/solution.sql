SELECT RANK() OVER(ORDER BY SUM(points) DESC),
       COALESCE(NULLIF(clan, ''), '[no clan specified]') AS clan,
       SUM(points) AS total_points,
       COUNT(*) AS total_people
FROM people
GROUP BY 2
ORDER BY 3 DESC;

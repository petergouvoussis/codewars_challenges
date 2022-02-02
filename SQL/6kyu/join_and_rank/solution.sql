SELECT RANK() OVER(ORDER BY COUNT(*) DESC) AS sale_rank,
       people.*,
       COUNT(*) AS sale_count
FROM people
JOIN sales ON people.id = sales.people_id
GROUP BY 2,3
ORDER BY 4 DESC;

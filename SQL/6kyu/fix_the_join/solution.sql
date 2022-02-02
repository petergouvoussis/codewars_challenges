SELECT
j.job_title,
CAST(ROUND(SUM(j.salary) / COUNT(*), 2) AS float) AS average_salary,
COUNT(p.id) AS total_people,
CAST(ROUND(SUM(j.salary), 2) AS float) AS total_salary
FROM people AS p JOIN job AS j ON p.id = j.people_id
GROUP BY j.job_title
ORDER BY average_salary DESC;

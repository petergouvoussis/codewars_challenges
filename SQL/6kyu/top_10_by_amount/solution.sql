SELECT p.customer_id, c.email, COUNT(*) AS payments_count, SUM(p.amount):: FLOAT AS total_amount FROM payment AS p
JOIN customer AS c ON p.customer_id = c.customer_id
GROUP BY 1,2
ORDER BY 4 DESC
LIMIT 10;

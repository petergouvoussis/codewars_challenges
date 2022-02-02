WITH special_sales AS (SELECT department_id FROM sales
                       WHERE price > 90)
SELECT id, name FROM departments
WHERE id IN (SELECT * FROM special_sales);

SELECT id, name FROM departments
WHERE EXISTS (SELECT * FROM sales WHERE departments.id = sales.department_id AND price > 98);

-- ORDER BY

-- Lowest to highest salary
SELECT *
FROM employees
ORDER BY salary ASC;

-- Highest to lowest salary
SELECT *
FROM employees
ORDER BY salary DESC;

-- Sort by age
SELECT *
FROM employees
ORDER BY age ASC;

-- Multiple-column sorting
SELECT *
FROM employees
ORDER BY department ASC, salary DESC;

-- Top 3 highest salaries
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;

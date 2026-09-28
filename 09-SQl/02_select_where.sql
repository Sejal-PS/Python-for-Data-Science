-- SELECT and WHERE

-- Select all employees
SELECT *
FROM employees;

-- Employees from IT
SELECT *
FROM employees
WHERE department = 'IT';

-- Employees earning more than 50000
SELECT name, salary
FROM employees
WHERE salary > 50000;

-- Employees younger than 30
SELECT name, age
FROM employees
WHERE age < 30;

-- Multiple conditions
SELECT *
FROM employees
WHERE department = 'IT'
AND salary > 50000;

-- OR condition
SELECT *
FROM employees
WHERE department = 'IT'
OR department = 'Finance';

-- BETWEEN
SELECT *
FROM employees
WHERE salary BETWEEN 50000 AND 65000;

-- IN
SELECT *
FROM employees
WHERE department IN ('IT', 'HR');

-- LIKE
SELECT *
FROM employees
WHERE name LIKE 'A%';

-- NOT EQUAL
SELECT *
FROM employees
WHERE department != 'IT';

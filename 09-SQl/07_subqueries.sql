-- SQL Subqueries

-- Employees earning more than average salary
SELECT
    name,
    salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);

-- Employee with highest salary
SELECT
    name,
    salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);

-- IT department employees
SELECT
    name,
    salary
FROM employees
WHERE department IN (
    SELECT department_name
    FROM departments
    WHERE department_name = 'IT'
);

-- Subquery in SELECT
SELECT
    name,
    salary,
    (
        SELECT AVG(salary)
        FROM employees
    ) AS company_average_salary
FROM employees;

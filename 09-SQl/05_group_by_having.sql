-- GROUP BY and HAVING

-- Employee count by department
SELECT
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department;

-- Average salary by department
SELECT
    department,
    AVG(salary) AS average_salary
FROM employees
GROUP BY department;

-- Highest salary by department
SELECT
    department,
    MAX(salary) AS highest_salary
FROM employees
GROUP BY department;

-- Departments with average salary above 50000
SELECT
    department,
    AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

-- Departments with at least two employees
SELECT
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) >= 2;

-- Common Table Expressions (CTE)

-- Department statistics
WITH department_salary AS (
    SELECT
        department,
        COUNT(*) AS employee_count,
        AVG(salary) AS average_salary
    FROM employees
    GROUP BY department
)
SELECT *
FROM department_salary;

-- CTE with filtering
WITH high_salary_employees AS (
    SELECT
        name,
        department,
        salary
    FROM employees
    WHERE salary > 50000
)
SELECT *
FROM high_salary_employees;

-- CTE with calculated results
WITH department_stats AS (
    SELECT
        department,
        COUNT(*) AS employee_count,
        AVG(salary) AS average_salary
    FROM employees
    GROUP BY department
)
SELECT
    department,
    employee_count,
    ROUND(average_salary, 2) AS average_salary
FROM department_stats
WHERE average_salary > 50000;

-- SQL Window Functions

-- ROW_NUMBER
SELECT
    name,
    department,
    salary,
    ROW_NUMBER() OVER (
        ORDER BY salary DESC
    ) AS salary_position
FROM employees;

-- RANK
SELECT
    name,
    department,
    salary,
    RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;

-- Rank employees within departments
SELECT
    name,
    department,
    salary,
    RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS department_rank
FROM employees;

-- Department average salary
SELECT
    name,
    department,
    salary,
    ROUND(
        AVG(salary) OVER (
            PARTITION BY department
        ),
        2
    ) AS department_average
FROM employees;

-- Difference from department average
SELECT
    name,
    department,
    salary,
    ROUND(
        salary -
        AVG(salary) OVER (
            PARTITION BY department
        ),
        2
    ) AS difference_from_average
FROM employees;

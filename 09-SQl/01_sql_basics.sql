-- SQL Basics
-- Beginner-friendly SQLite examples

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    department TEXT,
    salary REAL
);

INSERT INTO employees
(employee_id, name, age, department, salary)
VALUES
(1, 'Alice', 25, 'IT', 50000),
(2, 'Bob', 30, 'HR', 45000),
(3, 'Charlie', 28, 'IT', 60000),
(4, 'David', 35, 'Finance', 70000),
(5, 'Eva', 27, 'Marketing', 55000);

-- Display all records
SELECT *
FROM employees;

-- Display selected columns
SELECT name, department, salary
FROM employees;

-- Column aliases
SELECT
    name AS employee_name,
    salary AS annual_salary
FROM employees;

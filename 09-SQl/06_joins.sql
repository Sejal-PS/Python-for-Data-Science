-- SQL JOINs

DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT,
    location TEXT
);

INSERT INTO departments
(department_id, department_name, location)
VALUES
(1, 'IT', 'Pune'),
(2, 'HR', 'Mumbai'),
(3, 'Finance', 'Delhi'),
(4, 'Marketing', 'Bangalore');

-- INNER JOIN
SELECT
    e.name,
    e.department,
    d.location
FROM employees e
INNER JOIN departments d
    ON e.department = d.department_name;

-- LEFT JOIN
SELECT
    e.name,
    e.department,
    d.location
FROM employees e
LEFT JOIN departments d
    ON e.department = d.department_name;

-- JOIN with filtering
SELECT
    e.name,
    e.salary,
    d.location
FROM employees e
JOIN departments d
    ON e.department = d.department_name
WHERE e.salary > 50000;

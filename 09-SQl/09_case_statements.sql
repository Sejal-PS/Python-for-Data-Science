-- CASE Statements

-- Salary category
SELECT
    name,
    salary,
    CASE
        WHEN salary >= 65000 THEN 'High'
        WHEN salary >= 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category
FROM employees;

-- Age category
SELECT
    name,
    age,
    CASE
        WHEN age < 25 THEN 'Young'
        WHEN age <= 30 THEN 'Adult'
        ELSE 'Senior'
    END AS age_category
FROM employees;

-- Department type
SELECT
    name,
    department,
    CASE
        WHEN department = 'IT' THEN 'Technology'
        WHEN department = 'Finance' THEN 'Business'
        ELSE 'Other'
    END AS department_type
FROM employees;

-- Count high-salary employees by department
SELECT
    department,
    SUM(
        CASE
            WHEN salary >= 60000 THEN 1
            ELSE 0
        END
    ) AS high_salary_employees
FROM employees
GROUP BY department;

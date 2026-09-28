-- SQL String Functions

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER,
    name TEXT,
    city TEXT,
    email TEXT
);

INSERT INTO customers
VALUES
(1, 'Alice Smith', 'Pune', 'alice@example.com'),
(2, 'Bob Johnson', 'Mumbai', 'bob@example.com'),
(3, 'Charlie Brown', 'Delhi', 'charlie@example.com');

-- Uppercase
SELECT
    UPPER(name) AS name_uppercase
FROM customers;

-- Lowercase
SELECT
    LOWER(email) AS email_lowercase
FROM customers;

-- Remove spaces
SELECT
    TRIM(name) AS cleaned_name
FROM customers;

-- String length
SELECT
    name,
    LENGTH(name) AS name_length
FROM customers;

-- Find customers from Pune
SELECT *
FROM customers
WHERE city = 'Pune';

-- Extract part of a string
SELECT
    name,
    SUBSTR(name, 1, 5) AS short_name
FROM customers;

-- Search using LIKE
SELECT *
FROM customers
WHERE email LIKE '%example.com';

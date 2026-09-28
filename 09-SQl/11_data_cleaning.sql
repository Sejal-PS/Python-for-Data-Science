-- SQL Data Cleaning

DROP TABLE IF EXISTS messy_customers;

CREATE TABLE messy_customers (
    customer_id INTEGER,
    customer_name TEXT,
    city TEXT,
    age INTEGER,
    email TEXT
);

INSERT INTO messy_customers
VALUES
(1, ' Alice ', 'Pune', 25, 'alice@email.com'),
(2, 'Bob', 'Mumbai', 30, 'bob@email.com'),
(3, ' Alice ', 'Pune', 25, 'alice@email.com'),
(4, 'Charlie', ' pune ', NULL, 'charlie@email.com');

-- Find missing values
SELECT *
FROM messy_customers
WHERE age IS NULL;

-- Replace NULL values
SELECT
    customer_name,
    COALESCE(age, 0) AS age
FROM messy_customers;

-- Remove extra spaces
SELECT
    TRIM(customer_name) AS cleaned_name,
    TRIM(city) AS cleaned_city
FROM messy_customers;

-- Convert city to uppercase
SELECT
    UPPER(TRIM(city)) AS cleaned_city
FROM messy_customers;

-- Find duplicate records
SELECT
    customer_name,
    city,
    COUNT(*) AS record_count
FROM messy_customers
GROUP BY customer_name, city
HAVING COUNT(*) > 1;

-- Find invalid ages
SELECT *
FROM messy_customers
WHERE age < 0
   OR age > 100;

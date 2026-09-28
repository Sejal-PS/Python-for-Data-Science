-- SQL Date Functions
-- SQLite examples

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id INTEGER,
    customer_name TEXT,
    order_date TEXT,
    amount REAL
);

INSERT INTO orders
VALUES
(1, 'Alice', '2025-01-15', 5000),
(2, 'Bob', '2025-02-20', 7000),
(3, 'Charlie', '2025-03-10', 4500),
(4, 'David', '2025-03-25', 9000);

-- Display dates
SELECT
    order_id,
    order_date
FROM orders;

-- Extract year
SELECT
    order_id,
    strftime('%Y', order_date) AS year
FROM orders;

-- Extract month
SELECT
    order_id,
    strftime('%m', order_date) AS month
FROM orders;

-- Monthly sales
SELECT
    strftime('%Y-%m', order_date) AS month,
    SUM(amount) AS total_sales
FROM orders
GROUP BY month
ORDER BY month;

-- Orders after a specific date
SELECT *
FROM orders
WHERE order_date > '2025-02-01';

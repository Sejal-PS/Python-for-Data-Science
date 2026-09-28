-- SQL Data Analysis Project
-- Sales Data Analysis

DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    sale_id INTEGER,
    product TEXT,
    category TEXT,
    region TEXT,
    quantity INTEGER,
    price REAL,
    sale_date TEXT
);

INSERT INTO sales
VALUES
(1, 'Laptop', 'Electronics', 'West', 2, 50000, '2025-01-10'),
(2, 'Mobile', 'Electronics', 'West', 5, 20000, '2025-01-15'),
(3, 'Chair', 'Furniture', 'North', 10, 5000, '2025-02-05'),
(4, 'Laptop', 'Electronics', 'South', 3, 50000, '2025-02-20'),
(5, 'Table', 'Furniture', 'West', 4, 8000, '2025-03-01'),
(6, 'Mobile', 'Electronics', 'North', 6, 20000, '2025-03-12');

-- Calculate revenue
SELECT
    product,
    quantity,
    price,
    quantity * price AS revenue
FROM sales;

-- Total revenue
SELECT
    SUM(quantity * price) AS total_revenue
FROM sales;

-- Revenue by product
SELECT
    product,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;

-- Revenue by category
SELECT
    category,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- Revenue by region
SELECT
    region,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC;

-- Monthly revenue
SELECT
    strftime('%Y-%m', sale_date) AS month,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY month
ORDER BY month;

-- Best-selling products
SELECT
    product,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product
ORDER BY total_quantity DESC;

-- Products with revenue above 100000
SELECT
    product,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
HAVING SUM(quantity * price) > 100000;

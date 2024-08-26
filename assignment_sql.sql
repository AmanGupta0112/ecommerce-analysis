-- Question: Write a SQL query to find the top 5 customers who have spent the most money on the
-- platform. The output should include the following columns: customer_id, customer_name, email,
-- total_spent, and most_purchased_category (the category of products they spent the most money on).
SELECT
    c.customer_id,
    c.customer_name,
    c.email,
    SUM(oi.quantity * oi.price_per_unit) AS total_spent,
    MAX(p.category) AS most_purchased_category
FROM
    Customers c
    JOIN Orders o ON c.customer_id = o.customer_id
    JOIN Order_Items oi ON o.order_id = oi.order_id
    JOIN Products p ON oi.product_id = p.product_id
WHERE
    o.order_date >= DATE_SUB (CURDATE (), INTERVAL 1 YEAR)
GROUP BY
    c.customer_id,
    c.customer_name,
    c.email
ORDER BY
    total_spent DESC
LIMIT
    5;
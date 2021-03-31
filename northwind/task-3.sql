SELECT
    product_name, ROUND(SUM(order_details.unit_price * order_details.quantity) - SUM(order_details.quantity * order_details.discount*order_details.unit_price)) AS sum
FROM
    products
JOIN
    order_details
ON
    order_details.product_id = products.product_id
GROUP BY
    product_name
ORDER BY
    SUM(order_details.unit_price) ASC
LIMIT
    10

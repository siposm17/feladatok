SELECT
    date_part('year', order_date) as year,
    date_part('month', order_date) as month,
    COUNT(order_details.order_id) as count,
    ROUND(SUM(unit_price*quantity)-SUM(quantity*discount*unit_price)) as sum
FROM
    orders
JOIN
    order_details
ON
    orders.order_id = order_details.order_id
WHERE
    date_part('year', order_date) = 1997
GROUP BY
    year, month
ORDER BY
    month


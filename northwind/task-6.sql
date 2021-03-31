SELECT
    customers.company_name,
    COUNT(orders.order_id) as orders,
    string_agg(order_id::character varying, ', ') as order_ids
FROM
    customers
JOIN
    orders
ON
    orders.customer_id = customers.customer_id
WHERE
    ship_country = 'USA'
GROUP BY
    company_name
HAVING
    COUNT(orders.order_id) < 5
ORDER BY
    orders ASC

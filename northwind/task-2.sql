SELECT
    categories.category_name AS category, COUNT(categories.category_name) as number_of_products
FROM
    products
JOIN
    categories
ON
    products.category_id = categories.category_id
GROUP BY
    categories.category_name
ORDER BY
    number_of_products DESC, category
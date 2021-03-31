SELECT
    product_name as product, suppliers.company_name as company
FROM
    suppliers
JOIN
    products
ON
    products.supplier_id = suppliers.supplier_id
ORDER BY
    product ASC
SELECT
    country,
    COUNT(country) as count
FROM
    customers
GROUP BY
    country
HAVING
    COUNT(country) > 5
ORDER BY
    count DESC
# Northwind Traders

## Story

_Northwind Traders_ is a huge trading company which imports and exports
specialty foods from around the world. You are a member of the Data
Analysis team, and your task is to help the management to understand
what is going on in the company.

Here is the Entity-Relationship Diagram for the database.
![application process assignment.png](media/sql/northwind-ER.png)

## What are you going to learn?

- How to answer complex business questions using advanced SQL commands
- How to join database tables (`JOIN`)
- How to use aliases (`AS`)
- How to group results to use aggregated functions (`GROUP BY`, `COUNT`)
- How to order rows (`ORDER BY`)
- How to filter aggregated results (`HAVING`)
- How to use some PostgreSQL specific aggregate functions (`ARRAY_AGG`, `STRING_AGG`)

## Tasks

1. Your first task is to create a query to show which product is made by whom. Lists products and their suppliers. Display the `product_name` and the `company_name` of the supplier. Name result columns as `product` and `company` respectively. Order the results alphabetically by `product_name` and by `company_name`. Save your SQL query as `task-1.sql`.
    - The result of your query starts with the following lines:
```
     product      |           company
------------------+-----------------------------
Alice Mutton      | Pavlova, Ltd.
Aniseed Syrup     | Exotic Liquids
Boston Crab Meat  | New England Seafood Cannery
Camembert Pierrot | Gai pâturage
Carnarvon Tigers  | Pavlova, Ltd.
```
    - The result of your query contains 77 rows

2. Create a query to reveal how many products are in each category. List categories and number of products. Join tables `products` and `categories`. Name result columns as `category` and `number_of_products`, respectively. Order the results by the number_of_products descending and then by the category name. Save your SQL query as `task-2.sql`.
    - This is the result of your query:
```
    category       | number_of_products
    ---------------+--------------------
    Confections    |                 13
    Beverages      |                 12
    Seafood        |                 12
    Condiments     |                 12
    Dairy Products |                 10
    Grains/Cereals |                  7
    Meat/Poultry   |                  6
    Produce        |                  5
```
    - The result of your query contains 8 rows

3. The Head of Sales would like to know which products are the 10 worst performing ones. List product names and the total sum of the order values. Order the results by the `sum` column to start with the worst performing product. Save your SQL query as `task-3.sql`.
    - This is the result of your query:
```
           product_name     | sum
  --------------------------+------
  Chocolade                 | 1369
  Geitost                   | 1648
  Genen Shouyu              | 1785
  Laughing Lumberjack Lager | 2397
  Longlife Tofu             | 2433
  Gravad lax                | 2688
  Aniseed Syrup             | 3044
  Filo Mix                  | 3233
  Louisiana Hot Spiced Okra | 3383
  Valkoinen suklaa          | 3438
```
    - The result of your query contains 10 rows

4. Business developers would like to know the list of countries where there are more than 5 customers. Save your SQL query as `task-4.sql`.
    - This is the result of your query:
```
country | number_of_customers
--------+---------------------
USA     |                  13
France  |                  11
Germany |                  11
Brazil  |                   9
UK      |                   7
```
    - The result of your query contains 5 rows

5. Your CEO asks you to help her to create her end-of-year presentation. Provide her with the numbers for the year 1997 broken down by months. Save your SQL query as `task-5.sql`.
    - This is the result of your query:
```
year | month | order_count | revenue
-----+-------+-------------+---------
1997 |     1 |          85 |   61258
1997 |     2 |          79 |   38484
1997 |     3 |          77 |   38547
1997 |     4 |          81 |   53033
1997 |     5 |          96 |   53781
1997 |     6 |          76 |   36363
1997 |     7 |          77 |   51021
1997 |     8 |          84 |   47288
1997 |     9 |          95 |   55629
1997 |    10 |         106 |   66749
1997 |    11 |          89 |   43534
1997 |    12 |         114 |   71398
```
    - The result of your query contains 12 rows

6. Your colleague would like to manually check the printed order labels. So you have to create a sheet with all US customers who have less than 5 orders, display the total number of orders made by them, and also include a comma separated list of the order numbers. Save your SQL query as `task-6.sql`.
    - This is the result of your query:
```
          company_name            | orders |        order_ids
----------------------------------+--------+-------------------------
Lazy K Kountry Store              |      2 | 10482,10545
The Cracker Box                   |      3 | 10624,10775,11003
Trail's Head Gourmet Provisioners |      3 | 10574,10577,10822
Let's Stop N Shop                 |      4 | 10579,10719,10735,10884
The Big Cheese                    |      4 | 10310,10708,10805,10992
```
    - The result of your query contains 5 rows

## General requirements

None

## Hints

- You can find the SQL file with the sample data in the data folder.
  To use it, create a new database for this project and use `psql` to
  execute the SQL commands in that file:
    - Start `psql` in a terminal at the `data` folder of the project
    - Connect to your already created new database eg. `\connect northwind`
    - Execute the commands in the sql file `\i northwind_data.sql`
- When you calculate the value of an order make sure you are combining
  `product_price`, `quantity`, and `discount`.



## Background materials

- <i class="far fa-exclamation"></i> [Working with more complex data](project/curriculum/materials/pages/sql/sql-working-with-data.md)
- [Northwind database](https://www.geeksengine.com/article/northwind.html)
- <i class="far fa-book-open"></i> [Short guide about psql](http://postgresguide.com/utilities/psql.html)
- <i class="far fa-book-open"></i> [PostgreSQL documentation page about psql](https://www.postgresql.org/docs/current/app-psql.html)


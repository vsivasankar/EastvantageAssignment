import sqlite3

conn = sqlite3.connect('assignment.db')
cursor = conn.cursor()

sql_query = """
SELECT
    c.customer_id as Customer,
    c.age as Age,
    item_name as Item,
    CAST(SUM(quantity) AS INTEGER) as Quantity
FROM
    customers c
inner JOIN
    sales s ON c.customer_id = s.customer_id
inner JOIN
    orders o ON s.sales_id = o.sales_id
inner JOIN
    items i ON o.item_id = i.item_id
where
    c.age >= 18 AND c.age <= 35
group by 
    c.customer_id,o.item_id
"""
sql_results = cursor.execute(sql_query).fetchall()


# for row in sql_results:
#         print(", ".join(map(str, row)))
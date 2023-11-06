import sqlite3
import random

conn = sqlite3.connect('assignment.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        age INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE sales (
        sales_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    )
''')

cursor.execute('''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY,
        item_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        sales_id INTEGER,
        item_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY (sales_id) REFERENCES sales (sales_id),
        FOREIGN KEY (item_id) REFERENCES items (item_id)
    )
''')

customer_data = [(i, random.randint(18, 80)) for i in range(1, 10)]
sales_data = [(i, random.randint(1, 10)) for i in range(1, 10)]
item_data = [(1,'x'),(2,'y'),(3,'z')]
order_data = [(i, random.randint(1, 10), random.randint(1, 3), random.randint(1, 20)) for i in range(1, 15)]

cursor.executemany('INSERT INTO customers (customer_id, age) VALUES (?, ?)', customer_data)
cursor.executemany('INSERT INTO sales (sales_id, customer_id) VALUES (?, ?)', sales_data)
cursor.executemany('INSERT INTO items (item_id, item_name) VALUES (?, ?)', item_data)
cursor.executemany('INSERT INTO orders (order_id, sales_id, item_id, quantity) VALUES (?, ?, ?, ?)', order_data)

conn.commit()

conn.close()

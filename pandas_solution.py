import sqlite3
import pandas as pd

conn = sqlite3.connect('assignment.db')
cursor = conn.cursor()

df_customers = pd.read_sql_query("SELECT * FROM customers;", conn)
df_sales = pd.read_sql_query("SELECT * FROM sales;", conn)
df_items = pd.read_sql_query("SELECT * FROM items;", conn)
df_orders = pd.read_sql_query("SELECT * FROM orders;", conn)

# print(df_customers)
# print(df_sales)
# print(df_items)
# print(df_orders)


df = df_customers.merge(df_sales, on='customer_id', how='inner')
df = df.merge(df_orders, on='sales_id', how='inner')
df = df.merge(df_items, on='item_id', how='inner')

df = df[(df['age'] >= 18) & (df['age'] <= 35)]

df['quantity'] = df['quantity'].astype(int)

df = df.groupby(['customer_id','age','item_name'], as_index=False)['quantity'].sum()

df = df.rename(columns={
    'customer_id': 'Customer',
    'age': 'Age',
    'item_name': 'Item',
    'quantity': 'Quantity'
})

# print(df)

df.to_csv("output.csv", sep=';', index=False)

conn.close()

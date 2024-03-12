import psycopg2

# host='localhost'
# database='myduka'
# user='postgres'
# password='0777'
# port='5432'

# conecting to the PostgreSQL database
conn=psycopg2.connect(
    dbname='myduka',
    user='postgres',
    password='0777',
    host='localhost',
    port=5432
)
# # open a cursor to perfom database operation

cur = conn.cursor()

# def get_products():
#     cur.execute('select * from products;')
#     prods=cur.fetchall()
#     for i in prods:
#         print(i)
# # get_products()



# def get_sales():
#     select="select * from sales;"
#     cur.execute(select)
#     sales=cur.fetchall()
#     for i in sales:
#         print(i) 
    


# def insert_products():
#     insert="""INSERT INTO products( name, buying_price, selling_price, stock_quantity) 
#       VALUES ('airpods', 5000, 6000,233);"""
#     cur.execute(insert)
#     conn.commit()

# # insert_products()

# def insert_sales():
#     insert="""INSERT INTO sales( pid, quantity, created_at) 
#       VALUES ('5', 7,now());"""
#     cur.execute(insert)
#     conn.commit()
# insert_sales()
# get_sales()

def get_data(table):
    select=f"select * from {table};"
    cur.execute(select)
    data=cur.fetchall()
    return data
    # for i in data:
    #     print(i)

# function to insert products 
# def insert_products(values):
#     insert=f"""INSERT INTO products( name, buying_price, selling_price, stock_quantity)values{values}"""
#     cur.execute(insert)
#     conn.commit()
# products_value=('Mobile_charger',2500,3000,9)
# insert_products(products_value)

def insert_products(values):
    # place holders (%s)
    insert="""INSERT INTO products( name, buying_price, selling_price, stock_quantity)values(%s,%s,%s,%s)"""
    cur.execute(insert,values)
    conn.commit()
# products_value=('laptop_charger',2500,3000,9)

# insert_products(products_value)


# function to insert sales 
 
# def insert_sales(values):
#     insert=f"""INSERT INTO sales( pid, quantity, created_at)values{values},now()"""
#     cur.execute(insert)
#     conn.commit()
# sales_value=(12,14)
# insert_products(sales_value)
# get_data("products")
# get_data("sales")

def insert_sales(values):
    insert="""INSERT INTO sales( pid, quantity, created_at)values(%s,%s,now());"""
    cur.execute(insert,values)
    conn.commit()
# sales_values=(11,13)
# insert_sales(sales_values)
get_data("products")
# get_data("sales")

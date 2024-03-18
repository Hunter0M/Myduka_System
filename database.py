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

# to display products

# def get_products():
#     cur.execute('select * from products;')
#     prods=cur.fetchall()
#     for i in prods:
#         print(i)
# # get_products()


# to display sales 

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
#       VALUES (5, 7,now());"""
#     cur.execute(insert)
#     conn.commit()
# insert_sales()
# get_sales()

# 
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
    
def display_sales():
    display="select products.name, sum(selling_price*quantity) \
    as result from products join sales on sales.pid=products.id group by products.name;"
    cur.execute(display)
    data=cur.fetchall()
    return data
# display_sales()

def display_profit():
    display="select p.name,sum(((selling_price-buying_price)*quantity))\
          as profit from products as p join sales as s on s.pid=p.id group by p.name;"
    cur.execute(display)
    data=cur.fetchall()
    
    return data

def day_sales():
    d_sales=" SELECT DATE(created_at) AS date_only,sum(selling_price)\
        as total from sales as s join products as p on p.id=s.pid group by date_only order by date_only;"
    cur.execute(d_sales)
    data=cur.fetchall()
    return data

def pro_per_day():
    d_profit=" SELECT DATE(created_at) AS date_only,sum((selling_price-buying_price)*quantity)\
        as profits from sales as s join products as p on p.id=s.pid group by date_only order by date_only;"
    cur.execute(d_profit)
    data=cur.fetchall()
    return data


def register_user(values):
    insert="insert into users(full_name,email,password)values(%s,%s,%s)"
    cur.execute(insert,values)
    conn.commit()

def check_email(email):
    query='select exists(select 1 from users where email=%s)'
    cur.execute(query,(email,))
    exist=cur.fetchone()[0]
    return exist


get_data("products")
# get_data("sales")

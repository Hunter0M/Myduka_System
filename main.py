from flask import Flask,render_template,request,redirect,url_for
from database import get_data,insert_products,insert_sales,display_sales,display_profit,day_sales,pro_per_day\
    ,register_user,check_email

# creating an instance
app=Flask(__name__)

# creating a route for home page 
# @app.route('/')
@app.route("/")
def hello():
    return render_template('index.html')

# @app.route("/home")
# def home():
#     return "home page"

# creating a route for products page
@app.route("/products")
def products():
    prods=get_data("products")
    return render_template('products.html',prods=prods, title="Products")

@app.route('/add_products',methods=['POST'])
def add_products():
    p_name=request.form["product_name"]
    b_price=request.form["buying_price"]
    s_price=request.form["selling_price"]
    s_quantity=request.form["stock_quantity"]
    new_product=(p_name,b_price,s_price,s_quantity)
    insert_products(new_product)
    return redirect(url_for('products'))
    

# creating a route for sales
@app.route("/sales")
def sales():
    sales=get_data("sales")
    products=get_data("products")
    return render_template('sales.html',sales=sales,products=products,title="Sales")

@app.route("/make_sale",methods=['post','get'])
def make_sale():
    pid=request.form['pid']
    quantity=request.form['quantity']
    values=(pid,quantity)
    insert_sales(values)
    return redirect(url_for("sales"))

@app.route("/dashboard")
def dashboard():
    
    # route to display profit
    dash_profit=display_profit()
    names_profit=[]
    value_profit=[]
    for i in dash_profit:
        names_profit.append(str(i[0]))
        value_profit.append(float(i[1]))

   # route to display sales  
    dash_sales=display_sales()  
    names=[]
    value=[]
    for i in dash_sales:
        print(i)
        names.append(str(i[0]))
        value.append(float (i[1]))

    # route to display sales per a day 
    sales_day=day_sales()
    s_name=[]
    v_value=[]
    for i in sales_day:
        s_name.append(str(i[0]))
        v_value.append(float (i[1]))

    # route to display profit per day
        profit_day=pro_per_day()
        pro_name=[]
        pro_value=[]
        for i in profit_day:
            pro_name.append(str(i[0]))
            pro_value.append(float (i[1]))
    return render_template('dashboard.html',dash_sales=dash_sales,names=names,value=value,\
                           names_profit=names_profit,value_profit=value_profit,s_name=s_name,v_value=v_value,pro_name=pro_name,pro_value=pro_value)

@app.route("/register",methods=['POST','get'])
def register():
    if request.method=='POST':
        f_name=request.form['full_name']
        email=request.form['email']
        password=request.form['password']
        user=(f_name,email,password)
        if not check_email(email):
           register_user(user)
           return redirect(url_for('login'))
        else:
            return redirect(url_for('login')) 
    return render_template("register.html")

@app.route("/login",methods=['POST','get'])
def login():
    return render_template("login.html")

app.run(debug=True)


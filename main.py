from flask import Flask,render_template,request,redirect,url_for
from database import get_data,insert_products,insert_sales
app=Flask(__name__)

@app.route('/')
@app.route("/home")
def hello():
    return render_template('index.html')

# @app.route("/home")
# def home():
#     return "home page"

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
    return render_template('dashboard.html')


app.run(debug=True)


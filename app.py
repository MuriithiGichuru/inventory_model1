from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy  # import sqlalchemy

from configs.config import Development, Production

app = Flask(__name__)

app.config.from_object(Development)

db = SQLAlchemy(app)

from models.inventory import InventoryModel
from models.sales import SalesModel


@app.before_first_request
def create_table():
    db.create_all() #


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    inv = InventoryModel.query.all()

    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        stock = request.form['stock']
        serial_number = request.form['serial_number']
        reorder_point = request.form['reorder_point']

        #
        # print(name)
        # print(type)
        # print(buying_price)
        # print(selling_price)
        # print(stock)
        # print(serial_number)
        # print(reorder_point)


        inventory = InventoryModel(name=name, type=type, buying_price=buying_price, selling_price=selling_price,
                                   stock=stock, serial_number=serial_number, reorder_point=reorder_point)
        inventory.create_record()

        return redirect(url_for('inventory'))

    return render_template('inventory.html', x=inv)


@app.route('/sales', methods=['POST'])
def sales():
    s = SalesModel.query.all()

    if request.method == 'POST':
        quantity = request.form['quantity']
        inventory_id= request.form['inventory_id']

        # print(quantity)
        # print(inventory_id)

        sa = SalesModel(quantity=quantity, inventory_id=int(inventory_id))
        sa.create_record()

        InventoryModel.update_stock(int(inventory_id),int(quantity))



        print('sale suceesfully made')
        return redirect(url_for('inventory'))


    return redirect(url_for('inventory'))


@app.route('/view_sales/<int:id>',methods = ['GET'])
def view_sales(id):
    inve = InventoryModel.get_inventory_by_id(id)

    #print(inve.sale)
    #print(type(inve))

    sale_of_product = inve.sale

    return render_template('sales.html',s_o_p=sale_of_product)




if __name__ == '__main__':
    app.run(debug=True)

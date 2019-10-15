from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy #import sqlalchemy

# importing the configurations from the configs folder
from configs.config import Development,Production

# creating Flask instance
app = Flask(__name__)

# # setting/register the config class to be used
app.config.from_object(Development)

# sql-alchemy instance
db = SQLAlchemy(app)
#
# # Once created, that object then contains all the functions and helpers
# # from both sqlalchemy and sqlalchemy.orm.
# # Furthermore it provides a class called Model that is a declarative base
# # which can be used to declare models:
#
# # import the models
from models.inventory import InventoryModel
#from models.sales import salesModel

# use the decorator function called before-first-request to tell
# Flask-SQLAlchemy to create the tables before any request.

# to create or drop a table use the create_all() or drop_all() methods

@app.before_first_request
def create_table():
    db.create_all() #

@app.route('/')
def hello_world():

    # # # create a variable called myName
    # # myName = 'Gaideh'
    # #
    # # # create a list of cars
    # myCars = ['Toyota', 'subaru', 'Lambo']
    #
    # # for x in myCars:
    # #     print(x)
    #
    # thisdict = {
    #     "brand": "Ford",
    #     "model": "Mustang",
    #     "year": 1964
    # }
    #
    # print(thisdict.get('brand'))
    # print(thisdict['brand'])

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/inventory',methods=['GET', 'POST'])
def people():
    inv = InventoryModel.query.all()

    # POST method is used when you want to tell the server to accept
    # blocks of data, usually to create something.
    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        stock = request.form['stock']
        serial_number = request.form['serial_number']
        reorder_point = request.form['reorder_point']

        # to confirm whether we are actually getting user's input from
        # the html form, we print the variable name eg
        print(name)
        print(type)
        print(buying_price)
        print(selling_price)
        print(stock)
        print(serial_number)
        print(reorder_point)

        # create an instance of the PeopleModel class and pass in the data you want to send to the db
        inventory = InventoryModel(name=name, type=type, buying_price=buying_price, selling_price=selling_price,
                                   stock=stock, serial_number=serial_number, reorder_point=reorder_point)
        # call the create record method to insert the record in the database.
        inventory.create_record()

        return redirect(url_for('inventory'))
        #
        # #to confirm that we have actually inserted the record we are going to print out a string.
        # print('Imeingia')

    return render_template('inventory.html', x=inv)
#
# @app.route('/register', methods=['GET','POST'])
# def register():
#
#     return render_template('inventory.html')


if __name__ == '__main__':
    app.run()
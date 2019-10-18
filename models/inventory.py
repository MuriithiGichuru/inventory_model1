# import the db object from app.py file
from app import db

#use the Model class, which is the base declarative class used to declare your models
# # use Column() to define a column. the name of the column is the name that you assign it.
# # primary keys are marked using the primary_key=True
# # the type of column are passed in as the first arguinvement inside the Column() eg String(), Integer, DateTime etc
#
class InventoryModel(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    type = db.Column(db.String, nullable=False)
    buying_price = db.Column(db.Integer, nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    serial_number = db.Column(db.String, nullable=False)
    reorder_point = db.Column(db.String, nullable=False)
    sale = db.relationship('SalesModel', backref='inventory', lazy=True)

    # create
    def create_record(self):
        #db.drop_all(self)
        db.session.add(self)
        db.session.commit()

    #
    # @classmethod
    # def fetch_all(cls):
    #     return cls.query.all()






    # db.Integer
    # db.Float
    # db.Boolean
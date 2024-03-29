# import the db object from app.py file
from app import db

#use the Model class, which is the base declarative class used to declare your models
# # use Column() to define a column. the name of the column is the name that you assign it.
# # primary keys are marked using the primary_key=True
# # the type of column are passed in as the first argument inside the Column() eg String(), Integer, DateTime etc
#
class SalesModel(db.Model):

    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.String, nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)

    #id = db.Column(db.Integer, db.ForeignKey('id'), nullable=False)

    # create
    def create_record(self):
        db.session.add(self)
        db.session.commit()


    # @classmethod
    # def fetch_all(cls):
    #     return cls.query.all()








    # db.Integer
    # db.Float
    # db.Boolean
class Development:
    # databasename://user:password@host:port/dbname
    # eg postgresql://postgres:123456@127.0.0.1:5432/petManagementSystem
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@127.0.0.1:5432/inventory_system2'
    DEBUG = True
    SECRET_KEY = 'FSDJGLFDKJGLFKJG'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Production:
    pass
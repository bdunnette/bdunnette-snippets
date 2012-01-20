from storm.locals import *

class Product(object):
    __storm_table__ = "products"
    id = Int(primary=True)
    name = Unicode()
    price = Int()

database = create_database("mysql://root:test@localhost:3306/lemondb")
store = Store(database)
product = store.find(Product, Product.name == u"GeekBox").one()

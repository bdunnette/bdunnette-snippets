from storm.locals import *

class Person(object):
    __storm_table__ = "person"
    id = Int(primary=True)
    name = Unicode()

database = create_database("mysql://root:test@localhost:3306/lemondb")
store = Store(database)

from storm.locals import *

database = create_database("mysql://root:test@localhost:3306/lemondb")
store = Store(database)

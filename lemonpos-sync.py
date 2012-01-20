from storm.locals import *

database = create_database("mysql://root:test@localhost:3306/lemonpos")
store = Store(database)

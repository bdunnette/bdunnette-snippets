#!/usr/bin/python

import MySQLdb as lemondb
from proteus import config, Model
import sys

con = None

try:
    con = lemondb.connect(host="localhost", user="root", passwd="test", db="lemondb")
    config = config.set_xmlrpc("http://admin:test@localhost:8069/test")
    Product = Model.get('product.product')
    products = Product.find()
    for product in products:
        print product.code, product.name
    cur = con.cursor(lemondb.cursors.DictCursor)
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    for row in data:
        print "%s: %s (%s)" % (row["code"], row["name"], row["price"])
    
except lemondb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:
    #If connection to LemonPOS MySQL database is still open, close it
    if con:
        con.close()

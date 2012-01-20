#!/usr/bin/python

import MySQLdb as lemondb
import sys

con = None

try:
    con = lemondb.connect('localhost', 'root', 'test', 'lemondb')
    cur = con.cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    print data
    
except lemondb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:
    if con:
        con.close()

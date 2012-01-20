#!/usr/bin/python

import MySQLdb as lemondb
import psycopg2 as trytondb
import sys

lcon = None
tcon = None

try:
    lcon = lemondb.connect(host="localhost", user="root", passwd="test", db="lemondb")
    tcon = trytondb.connect(host="localhost", user="tryton", password="test", database="fgtc")
    cur = lcon.cursor(lemondb.cursors.DictCursor)
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    for row in data:
        print "%s: %s (%s)" % (row["code"], row["name"], row["price"])
    
except lemondb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:
    if lcon:
        lcon.close()

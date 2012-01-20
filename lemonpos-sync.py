#!/usr/bin/python

import MySQLdb as lemondb
import psycopg2 as trytondb
import sys

lcon = None
tcon = None

try:
    lcon = lemondb.connect('localhost', sys.argv[1], sys.argv[2], 'lemondb')
    tcon = trytondb.connect('localhost', 'tryton', 'test', 'fgtc')
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

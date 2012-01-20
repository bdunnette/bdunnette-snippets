#!/usr/bin/python

import MySQLdb as lemondb
import psycopg2 as trytondb
from proteus import config, Model
import sys

lcon = None
tcon = None

try:
    lcon = lemondb.connect(host="localhost", user="root", passwd="test", db="lemondb")
    config = config.set_xmlrpc('http://admin:test@localhost:8069/fgtc')
    Party = Model.get('party.party')
    party = Party.find([('name', '=', 'Buster Bot')])
    print party
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

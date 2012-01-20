#!/usr/bin/python
from proteus import config, Model, Wizard

config = config.set_xmlrpc('http://admin:test@localhost:8069/test')
Sale = Model.get('sale.sale')
sales = Sale.find()
for s in sales:
    print "%s: %s - %s" % (s.id, s.party.name, s.description)

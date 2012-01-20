#!/usr/bin/python
from proteus import config, Model, Wizard

config = config.set_xmlrpc('http://admin:test@localhost:8069/test')
Sale = Model.get('sale.sale')
sales = Sale.find()
print sales

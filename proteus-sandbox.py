#!/usr/bin/python
from proteus import config, Model, Wizard

config = config.set_xmlrpc('http://localhost:8069')
Party = Model.get('party.party')
party = Party.find([('name', '=', 'Buster Bot')])
print party
#!/usr/bin/python

import xmpp
import sys
import getpass

login = getpass.getuser()
pwd   = getpass.getpass()

cnx = xmpp.Client('jabber.umn.edu')

cnx.connect( server=('jabber.umn.edu', 5222))

cnx.auth(login, pwd, 'bot', sasl=0)

cnx.send(xmpp.Message("dunn0172@jabber.umn.edu", "Hello World from Python"))
#cnx.disconnect()

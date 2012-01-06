#!/usr/bin/python

from beancount.ledger import Ledger

ledger_file = open("fgtc-2011.journal")
ledger = Ledger()
ledger.parse_file('fgtc-2011.journal')

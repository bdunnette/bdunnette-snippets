#!/usr/bin/python

from beancount.ledger import Ledger

ledger_file = open("fgtc-2011.journal")
ledger = Ledger()
print ledger_file, ledger

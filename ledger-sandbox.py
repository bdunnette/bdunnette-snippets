#!/usr/bin/python

import sys
from beancount.ledger import Transaction, Ledger

ledger_file_name = sys.argv[1]
ledger_file_object = open(ledger_file_name)
ledger = Ledger()
ledger_parsed = ledger.parse_file(ledger_file_object, ledger_file_name, 'utf8')

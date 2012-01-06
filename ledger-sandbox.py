#!/usr/bin/python

import sys
from beancount.ledger import Transaction, Ledger
from beancount import cmdline

ledger_file_name = sys.argv[1]
ledger_file_object = open(ledger_file_name)
ledger = cmdline.load_ledger("", ledger_file_name, opts)
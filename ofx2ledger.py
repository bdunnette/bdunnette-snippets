#!/usr/bin/python

import sys
from ofxparse import OfxParser
import json

ofx = OfxParser.parse(file(sys.argv[1]))
print ofx.account.number
for transaction in ofx.account.statement.transactions:
    print transaction.date, transaction.id, transaction.memo, transaction.amount

account_file = file(sys.argv[2]).read() 
print account_file
dec = json.JSONDecoder()
accounts = dec.raw_decode(account_file)[0]['accounts']
for account in accounts:
    print account['ofx-account']

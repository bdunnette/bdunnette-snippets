#!/usr/bin/python

from relatorio.templates.opendocument import Template
from data import bonham_invoice
import sys

transaction_separator = "\n\n"

invoice = Template(source=None, filepath='invoice.odt')

infile = file(sys.argv[1]).read()
transactions = infile.split(transaction_separator)

for transaction in transactions:
    transaction_invoiced = False
    transaction_lines = transaction.splitlines()
    #The first line of each transaction is its overall description
    description_line = transaction_lines[0]
    #Check the remaining lines to see if this transaction has already been invoiced
    for line in transaction_lines[1:]:
        if line.strip().replace(' ','').startswith(';invoiced'):
            transaction_invoiced = True
        else:
            print line.strip(,1).split()
            
    print description_line, transaction_invoiced
    #invoice_generated = invoice.generate(o=ledger_invoice).render()
    #file(description_line + '.odt', 'wb').write(invoice_generated.getvalue())



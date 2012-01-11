#!/usr/bin/python

from relatorio.templates.opendocument import Template
from data import bonham_invoice
import sys

transaction_separator = "\n\n"

infile = file(sys.argv[1]).read()
transactions = infile.split(transaction_separator)

for transaction in transactions:
    transaction_invoiced = False
    transaction_lines = transaction.splitlines()
    #The first line of each transaction is its overall description
    description_line = transaction_lines[0]
    for line in transaction_lines:
        print line.strip()
        if line.strip().startswith(';invoiced'):
            print "Gouranga!"
            transaction_invoiced = True
            
    print description_line, transaction_invoiced
    
    

basic = Template(source=None, filepath='invoice.odt')
basic_generated = basic.generate(o=bonham_invoice).render()
#file('bonham_invoice.odt', 'wb').write(basic_generated.getvalue())



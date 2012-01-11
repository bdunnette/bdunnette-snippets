#!/usr/bin/python

from relatorio.templates.opendocument import Template
import sys

transaction_separator = "\n\n"

invoice_template = Template(source=None, filepath='invoice.odt')

infile = file(sys.argv[1]).read()
transactions = infile.split(transaction_separator)

for transaction in transactions:
    transaction_dict = dict()
    transaction_dict['invoiced'] = False
    transaction_amount = False
    transaction_lines = transaction.splitlines()
    #The first line of each transaction is its overall description
    description_line = transaction_lines[0]
    
    #Check the remaining lines to see if this transaction has already been invoiced
    for line in transaction_lines[1:]:
        if line.strip().replace(' ','').startswith(';invoiced'):
            transaction_dict['invoiced'] = True
        elif not transaction_amount and (len(line.rsplit('  ',1)) > 1):
            transaction_amount = line.rsplit('  ',1)[-1]
            
    print description_line, transaction_amount
    print transaction_dict
    invoice_generated = invoice_template.generate(invoice=transaction_dict).render()
    #file(description_line + '.odt', 'wb').write(invoice_generated.getvalue())



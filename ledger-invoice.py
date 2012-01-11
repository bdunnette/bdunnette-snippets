#!/usr/bin/python

from relatorio.templates.opendocument import Template
import sys

transaction_separator = "\n\n"
description_separators = ['|', ':']

invoice_template = Template(source=None, filepath='invoice.odt')

infile = file(sys.argv[1]).read()
transactions = infile.split(transaction_separator)

for transaction in transactions:
    transaction_dict = dict()
    transaction_dict['invoiced'] = False
    transaction_dict['total'] = False
    transaction_amount = False
    transaction_lines = transaction.splitlines()
    #The first line of each transaction is its overall description
    desc_line = transaction_lines[0].split(' ', 1)
    transaction_dict['date'] = desc_line[0]
    for sep in description_separators:
        print sep, desc_line
            
        if desc_line[1].find(sep):
            desc_split = desc_line[1].rsplit(sep)
            transaction_dict['customer'] = desc_split[0]
            transaction_dict['description'] = desc_split[1]
        else:
            transaction_dict['customer'] = desc_line[1]
    
    
    #Check the remaining lines to see if this transaction has already been invoiced
    for line in transaction_lines[1:]:
        if line.strip().replace(' ','').startswith(';invoiced'):
            transaction_dict['invoiced'] = True
        elif (not transaction_dict['total']) and (len(line.rsplit('  ',1)) > 1):
            transaction_dict['total'] = line.rsplit('  ',1)[-1]
            
    print desc_line, transaction_amount
    print transaction_dict
    #invoice_generated = invoice_template.generate(invoice=transaction_dict).render()
    #file(description_line + '.odt', 'wb').write(invoice_generated.getvalue())



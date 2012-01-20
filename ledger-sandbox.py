#!/usr/bin/python

import sys
import fileinput

transaction_separator = "\n\n"
description_separators = ['|', ':']

infile = file(sys.argv[1]).read()
transactions = infile.split(transaction_separator)

for transaction in transactions:
    transaction_dict = dict()
    transaction_dict['total'] = False
    transaction_dict['description'] = 'Miscellaneous Hardware'
    transaction_lines = transaction.splitlines()
    #The first line of each transaction is its overall description
    desc_line = transaction_lines[0].split(' ', 1)
    transaction_dict['date'] = desc_line[0]
    transaction_dict['party'] = desc_line[1]
    
    for sep in description_separators:
        if sep in desc_line[1]:
            desc_split = desc_line[1].split(sep)
            transaction_dict['party'] = desc_split[0].strip('* ')
            transaction_dict['description'] = desc_split[1].strip()
    
    for line in transaction_lines[1:]:
        if (not transaction_dict['total']) and (len(line.rsplit('  ',1)) > 1):
            transaction_dict['total'] = long(line.rsplit('  ',1)[-1])
            
    print transaction_dict

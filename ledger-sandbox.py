#!/usr/bin/python

import sys
import csv

transaction_separator = "\n\n"

infile = file(sys.argv[1]).read()
outfile = open((sys.argv[1] + '.csv'), 'wb')
csvwriter = csv.DictWriter(outfile, fieldnames=('date', 'code', 'party', 'description', 'total'))
csvwriter.writeheader()
transactions = infile.split(transaction_separator)

for transaction in transactions:
    transaction_dict = dict()
    transaction_dict['total'] = False
    transaction_dict['description'] = 'Miscellaneous Hardware'
    transaction_lines = transaction.splitlines()
    #The first line of each transaction is its overall description
    desc_line = transaction_lines[0].split(' ', 2)
    transaction_dict['date'] = desc_line[0]
    transaction_dict['code'] = desc_line[1].strip('(').strip(')')
    transaction_dict['party'] = desc_line[2].strip()
    
    if ':' in desc_line[2]:
        desc_split = desc_line[2].split(':')
        transaction_dict['party'] = desc_split[0].strip()
        transaction_dict['description'] = desc_split[1].strip()

    for line in transaction_lines[1:]:
        if (not transaction_dict['total']) and (len(line.rsplit('  ',1)) > 1):
            transaction_dict['total'] = float(line.rsplit('  ',1)[-1].strip('$'))
            
    csvwriter.writerow(transaction_dict)

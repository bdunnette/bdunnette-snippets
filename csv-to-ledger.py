#!/usr/bin/python

import sys
import csv
import string

try:
    csv_file = open(sys.argv[1])
    csv_reader = csv.DictReader(csv_file)
    fields = csv_reader.fieldnames
    print "Fields found: ", fields
    
    xml_file = open(sys.argv[2], "w")
    accounts = {}
    for row in csv_reader.reader:
        account_id = row[fields.index("ID")].strip()
        account_name = row[fields.index("Name")].strip()
        account_parent_id = row[fields.index("Parent")].strip()
        if account_parent_id in ('root', None):
            account_path = account_name
        else:
            account_path = accounts[account_parent_id]["path"] + ":" + account_name
        accounts[account_id] = {"name":account_name, "parent":account_parent_id, "path":account_path}
                
    print accounts

except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

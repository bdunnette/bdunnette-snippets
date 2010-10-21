#!/usr/bin/python

import csv
import xmlrpclib
import sys

#USER = sys.argv[1]
#PASSWORD = sys.argv[2]

csv_file = open("google.csv")
csv_reader = csv.DictReader(csv_file)
fields = csv_reader.fieldnames
    
# Get user_id and session
s = xmlrpclib.ServerProxy (sys.argv[1])

# Get the user context
context = s.model.res.user.get_preferences(True, {})

# Print all methods (introspection)
#print s.system.listMethods()

# Search parties and print rec_name
party_ids = s.model.party.party.search(
        [], # search clause
        0,  # offset
        10, # limit
        False, # order
        context)  # context

print s.model.party.party.read(
        party_ids, # party ids
        ['rec_name'], # list of fields
        context) # context
    
for line in csv_reader.reader:
    #groups = line[fields.index("Group Membership")].split(":::")
    new_party_name = str(line[fields.index("Name")])
    #party_id = s.model.party.party.search(["name","=",str(new_party_name)])
    #print party_id
    
    #if not party_id:
    new_party = {"name": new_party_name, "sequence": 1}
    party_id = s.model.party.party.create(new_party)

    for column in ("E-mail 1 - Value", "E-mail 2 - Value", "E-mail 3 - Value", "E-mail 4 - Value"):
        email_address = line[fields.index(column)]
        print email_address
        if email_address:
            new_email = {"party": party_id[1], "type": "email", "email": email_address}
            s.model.party.contact_mechanism.create(new_email)
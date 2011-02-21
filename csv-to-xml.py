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

    for row in csv_reader.reader:
        record = ""
        record += "<record model=\"account.account.template\" id=\"%s\">" % row[fields.index("Code")].strip()
        record += "<field name=\"name\">%s</field>" % row[fields.index("Name")].strip(" :").replace("&","and")
        record += "<field name=\"code\">%s</field>" % row[fields.index("Code")].strip()
        record += "<field name=\"kind\">%s</field>" % row[fields.index("Kind")].strip()
        if row[fields.index("Type")]:
            record += "<field name=\"type\">%s</field>" % row[fields.index("Type")].strip()
        record += "<field name=\"parent\" ref=\"%s\"/>" % row[fields.index("Parent")].strip()
        record += "</record>\n"
        #print record
        xml_file.write(record)

except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
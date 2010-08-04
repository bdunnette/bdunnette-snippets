#!/usr/bin/python

import sys, commands
from xml.dom.minidom import parse, parseString

try:
    #lshw_xml = commands.getoutput('/usr/bin/lshw -xml')
    #print lshw_xml
    infile = sys.argv[1]
    
    if infile:
        lshw_dom = parse(infile)    
    else:
        lshw_dom = parseString(lshw_xml)
    
    nodes = lshw_dom.getElementsByTagName("node")
    for node in nodes:
        print node
        if node.attributes:
            node_attrs = node.attributes
            for i in range(0, node_attrs.length):
                attr = node_attrs.item(i)
                print attr.name, attr.value
        else:
            print "No attributes found, skipping to next node..."
    
except:
    print "Unexpected error:", sys.exc_info()
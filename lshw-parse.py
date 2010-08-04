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
    
    nodes = lshw_dom.childNodes
    for node in nodes:
        
        if node.nodeType == node.COMMENT_NODE:
            print "COMMENT: ", node.nodeValue
        
        if node.nodeType == node.ELEMENT_NODE:
            print node, node.childNodes
        #    node_desc = node.getElementsByTagName("description")
        #    for desc in node_desc:
        #        print desc.nodeValue            
            
        if node.attributes:
            node_attrs = node.attributes
            for i in range(0, node_attrs.length):
                attr = node_attrs.item(i)
                print attr.name, attr.value
    
except:
    print "Unexpected error:", sys.exc_info()
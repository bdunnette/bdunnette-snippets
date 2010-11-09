#!/usr/bin/python
import xmlrpclib
import sys

endpoint = sys.argv[1]
server = xmlrpclib.ServerProxy(endpoint)

try:
    server_method_list = server.system.listMethods()
    print server_method_list
    server_method_help = ""
    for method in server_method_list:
        method_help = server.system.methodHelp(method)
        if method != "system.multicall":
            method_signature = server.system.methodSignature(method)
        else:
            method_signature = ""
        print method, method_help, method_signature
except xmlrpclib.ProtocolError, err:
    print "A protocol error occurred"
    print "URL: %s" % err.url
    print "HTTP/HTTPS headers: %s" % err.headers
    print "Error code: %d" % err.errcode
    print "Error message: %s" % err.errmsg
except xmlrpclib.Fault, err:
    print "A fault occurred"
    print "Fault code: %d" % err.faultCode
    print "Fault string: %s" % err.faultString



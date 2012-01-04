#!/usr/bin/python
import xmlrpclib
import sys

endpoint = sys.argv[1]
server = xmlrpclib.ServerProxy(endpoint)

try:
    server.__request('model.party.party.search', params)
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



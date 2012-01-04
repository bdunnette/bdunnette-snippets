#!/usr/bin/python
import xmlrpclib
import sys

try:
    endpoint = sys.argv[1]
    server = xmlrpclib.ServerProxy(endpoint)
    uid = sock_common.login(sys.argv[2], sys.argv[3], sys.argv[4])
    sock = xmlrpclib.ServerProxy(endpoint)

    args = [('name', '=', 'Buster Bot')]
    ids = sock.execute(sys.argv[2], uid, sys.argv[4], 'model.party.party', 'search', args)
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



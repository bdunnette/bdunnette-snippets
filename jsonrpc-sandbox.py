import jsonrpclib
server = jsonrpclib.Server('http://admin:test@localhost:8000')
methods = server.listMethods()
print methods

from jsonrpclib import Server as ServerProxy
import jsonrpclib
import json

server = ServerProxy('http://admin:test@localhost:8000')
try:
    server.common.db.list(None,None)
    a = json.loads(jsonrpclib.history.response)
    print(a["result"])
    
    server.common.db.create(None,None)
    a = json.loads(jsonrpclib.history.response)
    print(a["result"])

except:
    a = json.loads(jsonrpclib.history.response)
    print "error: ", a["error"]

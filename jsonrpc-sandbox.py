from jsonrpclib import Server as ServerProxy
import jsonrpclib
import json

server = ServerProxy('http://admin:test@localhost:8000')
try:
    server.common.db.list(None,None)
    a = json.loads( jsonrpclib.history.response)
    print(a["result"])

#!/usr/bin/python

import sys
import os
import hashlib
import mimetypes
from datetime import datetime
from couchdb.client import Server

server = Server(sys.argv[1])
db = server['wiki']

for file_path in sys.argv[2:]:
    file_date = os.path.getmtime(file_path)
    file_name = os.path.basename(file_path)
    f = open(file_path, 'r').read()
    file_md5 = hashlib.md5(f).hexdigest()
    file_doc = {}
    file_doc['type'] = 'file'
    file_doc['time'] = datetime.fromtimestamp(file_date).isoformat()
    file_doc['_id'] = file_md5
    file_doc['user'] = 'dunn0172'
    file_doc['name'] = file_name
    doc_id, doc_rev = db.save(file_doc)
    doc_attached = db.put_attachment(file_doc, f, file_name)
    print "File %s attached to document %s" % (file_name, doc_id)

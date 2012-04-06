#!/bin/sh
curl -X POST http://dunn0172:k1dn3y@localhost:5984/_replicate -d '{"source":"http://max.iriscouch.com/apps","target":"publicart", "doc_ids":["_design/recline"]}' -H "Content-type: application/json"
curl -X POST http://dunn0172:k1dn3y@localhost:5984/_replicate -d '{"source":"http://max.iriscouch.com/apps","target":"publicart", "doc_ids":["_design/geo"]}' -H "Content-type: application/json"
curl -X POST http://dunn0172:k1dn3y@localhost:5984/_replicate -d '{"source":"http://mertonium.iriscouch.com/apps","target":"publicart", "doc_ids":["_design/viewer"]}' -H "Content-type: application/json"

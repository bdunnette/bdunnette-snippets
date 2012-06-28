#!/usr/bin/python

import urllib2
import urllib
import json
import uuid
from couchdb.client import Server

server = Server()
try:
    db = server.create('cuke')
except:
    db = server['cuke']

baseurl = "http://api.jamendo.com/get2/"
jamendo_request = urllib2.urlopen('http://api.jamendo.com/get2/id+name+url+stream+artist_name+duration+album_id+album_mbid+album_name+artist_mbid+license_url+album_image/track/jsonpretty/track_album+album_artist/?n=50&order=ratingmonth_desc')
jamendo_json = jamendo_request.read()

top50 = json.loads(jamendo_json)
for track in top50:
    track['type'] = 'track'
    if track['artist_mbid'] == 0:
        del track['artist_mbid']
    if track['album_mbid'] == 0:
        del track['album_mbid']        
    if track['url']:
        track_uuid = uuid.uuid5(uuid.NAMESPACE_URL, str(track['url'])).hex
        track['_id'] = track_uuid
    doc_exists = db.get(track_uuid)
    if not doc_exists:
        doc_id, doc_rev = db.save(track)
        print "Added track %s (%s)" % (track['name'], doc_id)

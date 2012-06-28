#!/usr/bin/python

import urllib2
import uuid
import feedparser
from couchdb.client import Server

server = Server()
try:
    db = server.create('cuke')
except:
    db = server['cuke']

feeds = ['http://freemusicarchive.org/interesting.atom']
# for more music, include the 'recent' feed
#feeds.append('http://freemusicarchive.org/recent.atom')

for f in feeds:
    feed = feedparser.parse(f)
    for track in feed.entries:
        track_doc = {}
        track_doc['type'] = 'track'
        if track.enclosures:
            track_link = track.enclosures[0].href
            track_doc['stream'] = track_link
            track_uuid = uuid.uuid5(uuid.NAMESPACE_URL, str(track_link)).hex
            track_doc['_id'] = track_uuid
            track_doc['artist_name'] = track.author
            title_split = track.title.split(":")
            track_doc['album_name'] = title_split[1].strip()
            track_doc['name'] = title_split[2].strip()
        doc_exists = db.get(track_uuid)
        #print doc_exists, track_doc
        if not doc_exists:
            doc_id, doc_rev = db.save(track_doc)
            print "Added track %s (%s)" % (track_doc['name'], doc_id)

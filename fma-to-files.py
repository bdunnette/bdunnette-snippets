#!/usr/bin/python

import urllib2
import feedparser
from os.path import expanduser, exists 
from musicbrainz2.webservice import Query, TrackFilter, WebServiceError
from mutagen.id3 import ID3, UFID

feeds = []
# FMA's most 'interesting' tracks
feeds.append('http://freemusicarchive.org/interesting.atom')
# for a daily MP3...
#feeds.append('http://freemusicarchive.org/curator/FMA/blog.atom')
# for even more music, include the 'recent' feed
feeds.append('http://freemusicarchive.org/recent.atom')


home = expanduser("~")

for f in feeds:
    print "Parsing feed %s" % f
    feed = feedparser.parse(f)
    print feed
    for track in feed.entries:
        if track.enclosures:
            url = track.enclosures[0].href
            title_split = track.title.split(":")
            artist = title_split[0].replace("/",".").strip()
            album = title_split[1].replace("/",".").strip()
            title = title_split[2].replace("/",".").strip()
            file_name = home + "/Music/%s-%s-%s.mp3" % (artist, album, title)
            if exists(file_name):
                print "File %s already exists, skipping..." % file_name
            else:
                    
                u = urllib2.urlopen(url)
                f = open(file_name, 'wb')
                print "Downloading: %s" % file_name
                
                buffer = u.read()
                f.write(buffer)                
                f.close()

#!/usr/bin/python

import urllib2
import feedparser

feeds = []
feeds.append('https://commons.wikimedia.org/w/api.php?action=featuredfeed&feed=potd&feedformat=atom&language=en')

for f in feeds:
    print "Parsing feed %s" % f
    feed = feedparser.parse(f)
    print feed
    for picture in feed.entries:
	print "-----"
	for item in picture:
	    print item, picture[item]
	

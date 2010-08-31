#!/usr/bin/python

import time, re, sys, os, os.path, urlparse, urllib, codecs
import unicodedata
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

#The following code stolen from Clayton Parker's pyItunes -- http://github.com/liamks/pyitunes.git
class Song:
    """
    Song Attributes:
    name (String)
    artist (String)
    album_arist (String)
    composer = None (String)
    album = None (String)
    genre = None (String)
    kind = None (String)
    size = None (Integer)
    total_time = None (Integer)
    track_number = None (Integer)
    year = None (Integer)
    date_modified = None (Time)
    date_added = None (Time)
    bit_rate = None (Integer)
    sample_rate = None (Integer)
    comments = None (String)
    rating = None (Integer)
    album_rating = None (Integer)
    play_count = None (Integer)
    """
    name = None
    artist = None
    album_arist = None
    composer = None
    album = None
    genre = None
    kind = None
    size = None
    total_time = None
    track_number = None
    year = None
    date_modified = None
    date_added = None
    bit_rate = None
    sample_rate = None
    comments = None
    rating = None
    album_rating = None
    play_count = None
    location = None
    podcast = None

    #title = property(getTitle,setTitle)

class Library:
    def __init__(self, dictionary):
        self.songs = self.parseDictionary(dictionary)

    def parseDictionary(self, dictionary):
        songs = []
        format = "%Y-%m-%dT%H:%M:%SZ"
        for song, attributes in dictionary.iteritems():
            s = Song()
            s.name = attributes.get('Name')
            s.artist = attributes.get('Artist')
            s.album_artist = attributes.get('Album Artist')
            s.composer = attributes.get('Composer')
            s.album = attributes.get('Album')
            s.genre = attributes.get('Genre')
            s.kind = attributes.get('Kind')
            if attributes.get('Size'):
                s.size = int(attributes.get('Size'))
            s.total_time = attributes.get('Total Time')
            s.track_number = attributes.get('Track Number')
            if attributes.get('Year'):
                s.year = int(attributes.get('Year'))
            if attributes.get('Date Modified'):
                s.date_modified = time.strptime(attributes.get('Date Modified'), format)
            if attributes.get('Date Added'):
                s.date_added = time.strptime(attributes.get('Date Added'), format)
            if attributes.get('Bit Rate'):
                s.bit_rate = int(attributes.get('Bit Rate'))
            if attributes.get('Sample Rate'):
                s.sample_rate = int(attributes.get('Sample Rate'))
                s.comments = attributes.get("Comments ")
            if attributes.get('Rating'):
                s.rating = int(attributes.get('Rating'))
            if attributes.get('Play Count'):
                s.play_count = int(attributes.get('Play Count'))
            if attributes.get('Location'):
                s.location = attributes.get('Location')
            if attributes.get('Podcast'):
                s.podcast = attributes.get('Podcast')
            songs.append(s)
        return songs

class XMLLibraryParser:
    def __init__(self, xmlLibrary):
        f = open(xmlLibrary)
        s = f.read()
        lines = s.split("\n")
        self.dictionary = self.parser(lines)

    def getValue(self, restOfLine):
        value = re.sub("<.*?>", "", restOfLine)
        u = unicode(value, "utf-8")
        cleanValue = u.encode("ascii", "xmlcharrefreplace")
        return cleanValue

    def keyAndRestOfLine(self, line):
        rawkey = re.search('<key>(.*?)</key>', line).group(0)
        key = re.sub("</*key>", "", rawkey)
        restOfLine = re.sub("<key>.*?</key>", "", line).strip()
        return key, restOfLine

    def parser(self, lines):
        dicts = 0
        songs = {}
        inSong = False
        for line in lines:
            if re.search('<dict>', line):
                dicts += 1
            if re.search('</dict>', line):
                dicts -= 1
                inSong = False
                songs[songkey] = temp
            if dicts == 2 and re.search('<key>(.*?)</key>', line):
                rawkey = re.search('<key>(.*?)</key>', line).group(0)
                songkey = re.sub("</*key>", "", rawkey)
                inSong = True
                temp = {}
            if dicts == 3 and re.search('<key>(.*?)</key>', line):
                key, restOfLine = self.keyAndRestOfLine(line)
                temp[key] = self.getValue(restOfLine)
            if len(songs) > 0 and dicts < 2:
                return songs
        return songs

#end pyItunes code

def unquote(source):
	try:
		return urllib.unquote(str(source))
	except:
		return urllib.unquote(source)

try:
    itunesxml = os.path.expanduser("~/Music/iTunes/iTunes Music Library.xml")
    print "Using library file: ", itunesxml
    pl = XMLLibraryParser(itunesxml)
    l = Library(pl.dictionary)

    for song in l.songs:
        try:
            if ((song.name.find('-') > 0) or (song.name.find(':') > 0)) and not song.album:
                theURL = urlparse.urlparse(song.location)
                thePath = unquote(theURL.path)
                #audio = ID3(thePath)
                audio = MP3(thePath, ID3=EasyID3)
                #title_string = audio["title"].pop().encode('ascii', 'ignore')
                title_string = song.name
                title_stack = title_string.split("-")
                #print title_stack
                title_title = unicode(title_stack.pop().strip())
                title_artist = unicode(title_stack.pop().strip())
                print song.name, " => Artist:", title_artist, " Track:", title_title
                audio["title"] = title_title
                if (song.artist == 'MPR') or (not song.artist):
                    audio["artist"] = title_artist
                audio["album"] = ''
                audio["genre"] = ''
                audio.save()

        except:
            #print "Error in file: ", song.location, song.name
            continue


except:
    print "Unexpected error:", sys.exc_info()



#!/usr/bin/python

import urllib2

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('UMN', 'https://www.student.med.umn.edu/pathq/index.php', 'dunn0172', 'm_Tx0!td')
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)
page = urllib2.urlopen('https://www.student.med.umn.edu/pathq/index.php')
print page.read()
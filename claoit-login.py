#!/usr/bin/python

import getpass
import urllib2

base_url = "http://legacy.claoit.umn.edu/inout/claoit/index.php?controller=edit&action=set_in&userid="

current_user = getpass.getuser()

full_url = base_url + current_user
print full_url

signed_in = urllib2.urlopen(full_url)
print signed_in

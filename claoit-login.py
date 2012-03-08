#!/usr/bin/python

import getpass
import urllib2

base_url = "http://legacy.claoit.umn.edu/inout/claoit/index.php?controller=edit&action=set_in&userid="

# Get the current user, using the getpass module
current_user = getpass.getuser()

# Append the current username to the end of our base URL
full_url = base_url + current_user

# Fetch data from the full URL - in our case, simply doing a "GET" sets that user as "signed in"
signed_in = urllib2.urlopen(full_url)

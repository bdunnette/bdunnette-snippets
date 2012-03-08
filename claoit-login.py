#!/usr/bin/python

import getpass

base_url = "http://legacy.claoit.umn.edu/inout/claoit/index.php?controller=edit&action=set_in&userid="

current_user = getpass.getuser()
print base_url + current_user

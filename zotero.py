import sys
from pyzotero import zotero

zot = zotero.Zotero('23106', 'user', sys.argv[1])
items = zot.items()
# we have now retrieved the last five top-level items in our library
# we can print each item's item type and ID
for item in items:
    print 'Item Type: %s | Key: %s' % (item['itemType'], item['key'])

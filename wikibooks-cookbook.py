from simplemediawiki import MediaWiki
from couchdb.client import Server

server = Server()
try:
    db = server.create('feedme')
except:
    db = server['feedme']

wiki = MediaWiki('http://en.wikibooks.org/w/api.php')
recipes = wiki.call({'action': 'query', 'list': 'categorymembers', 'cmtitle': 'Category:Recipes', 'cmlimit': 'max'})
for recipe in recipes['query']['categorymembers']:
    recipe_doc = recipe
    doc_id, doc_rev = db.save(recipe_doc)
    print "Added recipe %s (%s)" % (recipe_doc['title'], doc_id)
    #recipe_content = wiki.call({'action': 'parse', 'text': '{{%s}}' % recipe['title']})
    #print recipe_content

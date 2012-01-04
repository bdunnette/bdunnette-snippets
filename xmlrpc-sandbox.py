import xmlrpclib

PASSWORD = 'test'
USER = 'admin'

# Get user_id and session
s = xmlrpclib.ServerProxy ('http://%s:%s@localhost:8069/test' % (USER, PASSWORD))

# Get the user context
context = s.model.res.user.get_preferences(True, {})

# Print all methods (introspection)
methods = s.system.listMethods()

# Search parties and print rec_name
party_ids = s.model.party.party.search(
        [('name', '=', 'Buster')], # search clause
        0,  # offset
        10, # limit
        False, # order
        context)  # context

print s.model.party.party.read(
        party_ids, # party ids
        ['rec_name'], # list of fields
        context) # context

# Execute report
#type, data, _ = s.report.party.label.execute(
#        party_ids, # party ids
#        {}, # data
#        context) # context
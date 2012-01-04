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
product_ids = s.model.product.product.search(
        [], # search clause
        0,  # offset
        10, # limit
        False, # order
        context)  # context

uoms = s.model.product.uom.search([], # search clause
        0,  # offset
        1000, # limit
        False, # order
        context)  # context

print s.model.product.uom.read(uoms, ['name', 'symbol'], context)

print s.model.product.product.read(
        product_ids, # party ids
        ['rec_name', 'code', 'sale_uom'], # list of fields
        context) # context

sale = s.model.sale.sale.create()
print sale

# Execute report
#type, data, _ = s.report.party.label.execute(
#        party_ids, # party ids
#        {}, # data
#        context) # context
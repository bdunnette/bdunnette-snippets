import ldap
l = ldap.initialize('ldap://ldap.umn.edu')
r = l.search_s('o=University of Minnesota,c=US',ldap.SCOPE_SUBTREE,'(mail=dunn01*)',[])
for dn,entry in r:
  print 'Processing',repr(dn)
  print entry

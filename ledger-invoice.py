#!/usr/bin/python

from relatorio.templates.opendocument import Template
from data import bonham_invoice
import sys

infile = file(sys.argv[1]).read()
transactions = infile.split('\n\n')
print transactions

basic = Template(source=None, filepath='invoice.odt')
basic_generated = basic.generate(o=bonham_invoice).render()
#file('bonham_invoice.odt', 'wb').write(basic_generated.getvalue())



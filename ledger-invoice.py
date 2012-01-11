#!/usr/bin/python

from relatorio.templates.opendocument import Template
from data import bonham_invoice

basic = Template(source=None, filepath='basic.odt')
basic_generated = basic.generate(o=bonham_invoice).render()
file('bonham_basic.odt', 'wb').write(basic_generated.getvalue())



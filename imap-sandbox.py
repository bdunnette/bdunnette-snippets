import getpass
import imaplib
from email.parser import Parser

M = imaplib.IMAP4_SSL("imap.gmail.com")
M.login("bdunnette@gmail.com", getpass.getpass())
M.select()
message_parser = Parser()
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    message = message_parser.parsestr(data[0][1])
    print message.get_payload()
    #print 'Message %s\n%s\n' % (num, data[0][1])
M.close()
M.logout()

# pip install imapclient
# easy_install pyzmail

# Checking your email from Python
import imapclient
comm = imapclient.IMAPClient('imap.yahoo.com', ssl=True)
conn.login('email', 'password')
conn.select_folder('INBOX', readonly=TRUE)
UIDs = conn.search(['SINCE 20-Aug-2015'])
raw_message = conn.fetch([id you want], ['BODY[]', 'FLAGS'])

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[uid you want][b'BODY[]'])

message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')
print(message.text_part)
message.text_part.get_payload().decode('UTF-8') # it's usually UTF-8

conn.list_folders()

conn.select_folder('INBOX', readonly=FALSE) # warning - you can delete things this way


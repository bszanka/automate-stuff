import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('simplifybanking@gmail.com', 'password')
conn.select_folder('INBOX', readonly=True)
# Search e-mails since 2022-09-12.
# Search syntax: https://imapclient.readthedocs.io/en/master/#imapclient.IMAPClient.search
UIDs = conn.search(['SINCE', '12-Sep-2022'])
print(UIDs)
# The message's (UID: 53) Body (binary) and Flags.
rawMessage = conn.fetch([52], ['BODY[]', 'FLAGS'])
print(rawMessage.items())

# Parse the message using the pyzmail module. We want the BODY of the message (UID: 53).
message = pyzmail.PyzMessage.factory(rawMessage[52][b'BODY[]'])
# We print out the subject and the message's text part.
print(message.get_subject())
print(message.text_part.get_payload().decode('UTF-8'))

# Delete a message.
# print(conn.list_folders())
# conn.select_folder('INBOX', readonly=False)
# conn.delete_messages(rawMessage) # I could just pass the 'UIDs' variable too.

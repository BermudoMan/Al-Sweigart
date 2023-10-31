import imapclient
#import pizmail

imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
print(imap_obj)
#print(smtp_obj.login('ivankurochkin95@bk.ru', 'my_password'))
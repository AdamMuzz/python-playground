#dependencies
import os
import csv
import time
import smtplib
from email.message import EmailMessage


#optionally load email template from source file
'''
script_dir = os.path.dirname(__file__)
rel_path = 'email-template.txt'
file_path = os.path.join(script_dir, rel_path)

with open(file_path) as file:
	msg = EmailMessage()
	msg.set_content(file.read())
'''


#email service setup
user = 'username@gmail.com'
password = '********'
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(user, password)


#generating emails
file_path = 'path/to/file'
with open(file_path) as data:
	for (first, last, addr) in csv.reader(data):
		msg = EmailMessage()
		msg.set_content(f'''Dear {first},

This is an example of using data from a csv to batch generate custom emails.


Best,
Adam Muzzarelli
''')
		msg['Subject'] = f'The contents of {file_path}'
		msg['From'] = 'username@gmail.com'
		msg['Cc'] = 'optional@gmail.com'
		msg['To'] = addr
		s.send_message(msg)
		time.sleep(0.1)			#sleep for 100 ms to avoid Google API limit


#cleanup
s.quit()
print('Sent emails successfully!')
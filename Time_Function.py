import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import datetime

def test():
    with open('1.txt', 'r') as f:
       for line in f:
         x = datetime.datetime.now()
         temp = line.rstrip('\n')
         print(temp)
         time.sleep(5)
         fromaddr = "MY_EMAIL@cock.li"
         toaddr = "TARGETS_EMAIL"

         msg = MIMEMultipart()

         msg['From'] = fromaddr
         msg['To'] = toaddr
         msg['Subject'] = x.strftime("%X")
		
         body = temp



         msg.attach(MIMEText(body, 'plain'))


         server = smtplib.SMTP('mail.cock.li', 587)
         server.starttls()
         server.login(fromaddr, "MY_PASSWORD")
         text = msg.as_string()
         server.sendmail(fromaddr, toaddr, text)
         server.quit()
         

numberEmails = 1

for _ in range(numberEmails):
    test()

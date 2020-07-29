import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time

def test():
    with open('1.txt', 'r') as f:
       for line in f:
         temp = line.rstrip('\n')
         print(temp)
         time.sleep(5)
         fromaddr = "MY_EMAIL"
         toaddr = "TARGETS_EMAIL"

         msg = MIMEMultipart()

         msg['From'] = fromaddr
         msg['To'] = toaddr
         msg['Subject'] = "haha"
		
         body = temp



         msg.attach(MIMEText(body, 'plain'))


         server = smtplib.SMTP('smtp.gmail.com', 587)
         server.starttls()
         server.login(fromaddr, "MY_PASSWORD")
         text = msg.as_string()
         server.sendmail(fromaddr, toaddr, text)
         server.quit()
         

numberEmails = 5

for _ in range(numberEmails):
    test()

#!/usr/bin/python
import os, re
import sys
import smtplib
import email.utils
 
#from email.mime.image import MIMEImage
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.MIMEText import MIMEText

 
SMTP_SERVER = '#smtp server#'
SMTP_PORT = #smtp port#

 
sender = '#sender#'
password = "#sender password#"
recipient = ['#recipient1#', '#recipient2#']
subject = 'MODIFICATION IN SITE'
message = 'PLEASE CHECK THE FILE'
 
def main():
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['To'] = ','.join(recipient)
    msg['From'] = sender
    
    
    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)
    
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
    session.ehlo()
    session.starttls()
    session.ehlo
    
    session.login(sender, password)

    fp = open('dout', 'rb')
    msgq = MIMEBase('text', 'text')
    msgq.set_payload(fp.read())
    fp.close()
    # Encode the payload using Base64
    encoders.encode_base64(msgq)
    # Set the filename parameter
    filename='dout'
    msgq.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(msgq)
    # Now send or store the message
    qwertyuiop = msg.as_string()



    session.sendmail(sender, recipient, qwertyuiop)
    
    session.quit()
    os.system('notify-send "Email sent"')
 
if __name__ == '__main__':
    main()

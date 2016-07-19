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

 
SMTP_SERVER = '#smtp server#'             #Enter SMTP server details here
SMTP_PORT = #smtp port#			  #Enter SMTP port details here

 
sender = '#sender#'			  #Enter Sender Email Id here
password = "#sender password#"		  #Enter Sender Password here
recipient = ['#recipient1#', '#recipient2#']   #Enter Email Ids of Sender1, Sender2 and so on
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
    filename='dout'
    msgq.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(msgq)
    qwertyuiop = msg.as_string()



    session.sendmail(sender, recipient, qwertyuiop)
    
    session.quit()
    os.system('notify-send "Email sent"')
 
if __name__ == '__main__':
    main()

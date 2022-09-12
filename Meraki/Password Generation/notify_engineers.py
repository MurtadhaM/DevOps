"""
from pydoc import describe
Author: Murtadha Marzouq
Description: This script is used to send an email to the engineers using an SMRP reley and OAuth2 authentication
Date: 09-10-2022
"""
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib




def send_email(subject, msg, HOST, PORT, USERNAME, MAILTO, APP_PASSWORD, ATTACHMENT):
    try:
        server = smtplib.SMTP('${HOST}:${PORT}')
        server.ehlo( )
        server.starttls()
        server.login(USERNAME, APP_PASSWORD)
        
        message = "From: InfraStruction Mailer <${USERNAME}> To: ${MAILTO} Subject: ${subject} ${msg}"
      # MESSAGE TO BE SENT
    except Exception as e:   
        print("Error: unable to send email")
        print(e)
    print("Successfully sent email")

def send_email_with_attachment(subject, message, HOST, PORT, USERNAME, MAILTO, APP_PASSWORD, ATTACHMENT):
    try:
        with open(ATTACHMENT, 'rb') as f:
            img_data = f.read()

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = USERNAME
        msg['To'] = MAILTO
        text = MIMEText(message)
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename(ATTACHMENT))
        msg.attach(image)
        
        s = smtplib.SMTP(HOST, PORT)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(USERNAME, APP_PASSWORD)
        s.sendmail(USERNAME, MAILTO, msg.as_string())
        s.quit()

    except Exception as e:
        print('Error: unable to send email attachment')
        print(e)    
    print("Successfully sent email")


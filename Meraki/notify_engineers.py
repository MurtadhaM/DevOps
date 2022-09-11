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

# Variables to be used
HOST = "smtp.gmail.com"
PORT = 587
USERNAME = "mmarzouq@uncc.edu"
# ANOTHER WAY TO SEND EMAIL
tolist= ["email1@email.com", "email2@email.com"]
# MAIL To Address
MAILTO = "mmarzouq@wastequip.com"
# NOTE: For gmail account with 2FA , you need to generate apps to be able to send emails
# https://myaccount.google.com/apppasswords
APP_PASSWORD = ""



def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo( )
        server.starttls()
        server.login(USERNAME, APP_PASSWORD)
        
        message = "From: InfraStruction Mailer <mmarzouq@uncc.edu>
        To: ${MAILTO}
        Subject: ${subject}
        ${msg}"
        # MESSAGE TO BE SENT
    except Exception as e:   
        print("Error: unable to send email")
        print(e)
    
    print("Successfully sent email")

def send_email_with_attachment(subject, msg, ImgFileName):
    try:
        with open(ImgFileName, 'rb') as f:
            img_data = f.read()

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = USERNAME
        msg['To'] = ""
        text = MIMEText("test")
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        msg.attach(image)
        s = smtplib.SMTP("smtp.gmail.com", PORT)
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


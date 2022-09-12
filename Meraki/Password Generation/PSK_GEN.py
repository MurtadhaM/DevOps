"""
Author: Murtadha Marzouq
Description: This script is used generate a random password and build an image to be shared with company's employees
Date: 09-10-2022
"""


import os
from passlib.utils import pbkdf2
import binascii, sys
import random
import subprocess
import wifi_qrcode_generator
from passlib.utils import pbkdf2
import binascii, sys
import random
import string



def generateRandomPassword(ssid, password):
    # Generate random password
    PSK_KEY = pbkdf2.pbkdf2(str.encode(password), str.encode(ssid), 4096, 32)
    PSK_KEY_HEX = binascii.hexlify(PSK_KEY).decode("utf-8")
    PSK_KEY_BASE = binascii.b2a_base64(PSK_KEY).decode("utf-8")
    return PSK_KEY_HEX, PSK_KEY_BASE
def generate_random_password():
    # Generate random password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(9))
    return password
    
    
def generateQRCode(ssid, password):
    # Generate QR code
    try:
        # Create a QR code for the SSID and password    
        QR_IMAGE =     wifi_qrcode_generator.wifi_qrcode(ssid, False, 'WPA', password)
        # Save the QR code to a file
        QR_IMAGE.save('QR.png')

    except Exception as e:
        print("something wrong")
        print(e)
     

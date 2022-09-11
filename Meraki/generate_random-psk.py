"""
Author: Murtadha Marzouq
Description: This script is used generate a random password and build an image to be shared with company's employees
Date: 09-10-2022
"""


from passlib.utils import pbkdf2
import binascii, sys
import random
import subprocess
# try catch block begns
# try block
try:

PASSWORD: 7045747748
SSID: Food Stamps


   
    # traverse the profile
    Id = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')
    id_results = str([b.split(":")[1][1:-1]
                      for b in Id if "Profile" in b])[2:-3]

    # traverse the password
    password = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profiles',
         id_results, 'key=clear']).decode('utf-8').split('\n')
     
    pass_results = str([b.split(":")[1][1:-1]
                        for b in password if "Key Content" in b])[2:-2]
    print("User name :", id_results)
    print("Password :", pass_results)
     
except:
    print("something wrong")
     
# generate Qr code
wifi_qrcode_generator.wifi_qrcode(id_results, False, 'WPA', pass_results)


    """
    
    WHERE I STOPPED: I NEED TO PRINT THE QR CODE TO A FILE AND SEND IT TO THE EMPLOYEE'S EMAIL 
    
    """

# Getting the functions from the other script
from  PSK_GEN import *
from notify_engineers import *

# Variables to be used
HOST = "smtp.gmail.com"
PORT = 587
USERNAME = "mmarzouq@uncc.edu"
# MAIL To Address
MAILTO = "mmarzouq@wastequip.com"
APP_PASSWORD = ""
ATTACHMENT = "QR.png"
SUBJECT = "WIFI QR CODE"



random_password = generate_random_password()
generateQRCode("WQ_Guest", random_password)
MSG =f'WIFI Network: WQ_GUEST\nPassword: ${random_password}'

# POSITIONAL ARGUMENTS
#subject, msg, HOST, PORT, USERNAME, MAILTO, APP_PASSWORD, ATTACHMENT
send_email_with_attachment(SUBJECT, MSG, HOST, PORT, USERNAME, MAILTO, APP_PASSWORD, ATTACHMENT)




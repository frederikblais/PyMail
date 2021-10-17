import os
import smtplib
import ssl
from datetime import datetime
from colorama import Fore, Style
from dotenv import load_dotenv

load_dotenv()
sender_email = os.getenv('username')
receiver_email = os.getenv('receiver')

# path_to_email = 'src/emails/email.txt'

# with open(path_to_email, 'r') as f:
#     contents = f.readlines()

message = """\
Subject: Hi there

[Content here]

Sent from PyMail."""


port = 465  # For SSL
os.system('clear')
# password = os.getenv('password')
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:

    try:
        server.login(sender_email, password)

        print()
        print(f'[{Fore.GREEN}SUCCESS{Style.RESET_ALL}] Connected to IMAP server.')
        print(f'[{Fore.GREEN}SUCCESS{Style.RESET_ALL}] Sending email...')

        server.sendmail(sender_email, receiver_email, message)

        get_time = datetime.now()
        current_time = get_time.strftime("%H:%M:%S")

        print()
        print('Sent to: ', receiver_email)
        print()
        print('Time: ', current_time)
        print()
        print('Message: ')
        print(message)
    except:
        print()
        print(f'[{Fore.RED}ERROR{Style.RESET_ALL}] Incorrect credentials.')
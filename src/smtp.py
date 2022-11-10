# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from src.config import EMAIL, PASSWORD, SERVER


# create message object instance


class Smtp:
    def __init__(self, receiver):
        self.msg = MIMEMultipart()
        self.password = PASSWORD
        self.msg['From'] = EMAIL
        self.msg['To'] = receiver

    def send_email(self, content_msg, subject):
        message = content_msg

        # setup the parameters of the message
        self.msg['Subject'] = subject

        # add in the message body
        self.msg.attach(MIMEText(message, 'plain'))

        # create server
        server = smtplib.SMTP(SERVER)

        server.starttls()

        # Login Credentials for sending the mail
        server.login(self.msg['From'], self.password)

        # send the message via the server.
        server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())

        server.quit()

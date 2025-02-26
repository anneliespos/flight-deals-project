import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_TOKEN"])
        #twilio sid and authentication token stored in .env file

    def send_sms(self, message_body):
        """Send sms when cheap flight is found"""
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VERIFIED_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)


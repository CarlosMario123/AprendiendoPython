from dotenv import load_dotenv
import os
from twilio.rest import Client
load_dotenv()

tw_sid = os.getenv("TWILIO_SID")
tw_token = os.getenv("TWILIO_TOKEN")
tw_phone = os.getenv("TWILIO_PHONE")
cliente = Client(tw_sid, tw_token)

message = cliente.messages.create(
    body="hola mundo",
    from_ = tw_phone,
    to ="numero a enviar"
)

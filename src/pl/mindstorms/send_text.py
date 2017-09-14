# import twilio
# print(twilio.__version__)

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to = "",    # Your live phone num
    from_= "",   # Your Twilio phone num
    body = "")

print(message.sid)
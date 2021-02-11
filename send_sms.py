from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""

# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

# To and From are phone numbers
message = client.messages.create(
    to="", 
    from_="",
    body="This is a simple message sent using Twilio_API")

print(message.sid)

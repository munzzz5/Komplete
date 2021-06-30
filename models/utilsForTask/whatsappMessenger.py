from twilio.rest import Client

account_sid = 'ACC SID'
auth_token = 'AUTH TOKEN'
client = Client(account_sid, auth_token)
api_key = 'APIKEY'
message = client.messages.create(
    from_='whatsapp:+13124677853',
    body='Your appointment is coming up on July 21 at 3PM',
    to='whatsapp:+917530005800'
)

print(message.sid)

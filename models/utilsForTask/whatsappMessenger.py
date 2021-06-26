from twilio.rest import Client

account_sid = 'AC57b5b2abed9c0e4b2f31daef947dfecf'
auth_token = 'a78f3259eaca573c752940b630978957'
client = Client(account_sid, auth_token)
api_key = 'SK5d8913a0fe198725de565d6caac74273'
message = client.messages.create(
    from_='whatsapp:+13124677853',
    body='Your appointment is coming up on July 21 at 3PM',
    to='whatsapp:+917530005800'
)

print(message.sid)

from twilio.rest import Client
import os

account_sid = 'AC967e6c6fca539a3fcd54e62cefa5016b'
auth_token = '4a3ad7cc558be0f8c75e1ae3dd1ffb81'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+19388002828',
  to='+9779741897738',
  body='Hello its me Prashant'
)

print(message.sid)
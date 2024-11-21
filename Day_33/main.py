import requests
import lxml
from bs4 import BeautifulSoup
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9"
}
response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6" , headers= header)
# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
price = soup.find("span" , attrs= {"class" : "a-price-fraction"})
# print(price.text)




from twilio.rest import Client
import os
# This is how we can put key in environment go to cmd and type this ----      account_sid = 'AC967e6c6fca539a3fcd54e62cefa5016b'
# TO excess use os and then as below:


account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

client = Client(account_sid, auth_token)

if int(price.text) <= 100:
    message = client.messages.create(
    from_='+13182258037',
    body= f'Hey the value of your product just reached the limit price of {price.text}',
    to='+9779741897738'
    )

print(message.sid)
    
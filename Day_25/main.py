import requests
import datetime as dt

today_stock_key = "2024-08-01"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ACCESS_KEY =  ""
NEWS_API = ""
STOCK_PARAMETER ={
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "TSLA",
    "apikey" : ACCESS_KEY
}
NEWS_PARAMETER ={
    "q":"TSLA",
    "from": today_stock_key,
    "to": today_stock_key,
    "apikey" : NEWS_API

}
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
def get_news():
    pass


# TO GET STOCK CHANGE
response = requests.get(url= STOCK_ENDPOINT , params = STOCK_PARAMETER)

data = response.json()
daily_stock = data['Time Series (Daily)']
today_stock_key= list(daily_stock.keys())[0]
today_closing = float(daily_stock[today_stock_key]['4. close'])


yesterday_stock_key= list(daily_stock.keys())[1]
yesterday_closing = float(daily_stock[yesterday_stock_key]['4. close'])

percentage_change = ((today_closing - yesterday_closing)/yesterday_closing)*100

if abs(percentage_change) >= 5:
    get_news()







# print(titles)
# print(description)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
def get_news():
    # Fetching news from news api
    response = requests.get(url = NEWS_ENDPOINT, params = NEWS_PARAMETER)
    data = response.json()
    titles = [article['title'] for article in data['articles'][:3]]
    description = [article['description'] for article in data['articles'][:3]]

    # NOW USING TWILIO API TO SEND MESSAGE

    from twilio.rest import Client

    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    if percentage_change > 0:

        message = client.messages.create(
        from_='',
        to='',
        body= f"""TSLA: 🔺{abs(percentage_change)}%
            Headline: {titles[0]}
            Body: {description[0]}

            Headline: {titles[1]}
            Body: {description[1]}

            Headline: {titles[2]}
            Body: {description[2]}"""
        )

        print(message.sid)

    else:
        message = client.messages.create(
        from_='+',
        to='+',
        body= f"""TSLA: 🔻{abs(percentage_change)}%
            Headline: {titles[0]}
            Body: {description[0]}

            Headline: {titles[1]}
            Body: {description[1]}

            Headline: {titles[2]}
            Body: {description[2]}"""
        )



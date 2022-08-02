import datetime as dt
import requests
import math
from twilio.rest import Client


def previous_bussiness_day(date: dt.date):
    while True:
        date -= dt.timedelta(days=1)
        if date.weekday() not in (5, 6):
            break
    return date


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "Your key"
STOCKS_API_URL = "https://www.alphavantage.co/query"
NEWS_API_KEY = "Your key"
NEWS_API_URL = "https://newsapi.org/v2/everything"
account_sid = "your_sid"
auth_token = "your_auth_token"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': STOCK_API_KEY,
}

today = dt.date.today()
yesterday = previous_bussiness_day(today)
before_yesterday = previous_bussiness_day(yesterday)

stock_response = requests.get(STOCKS_API_URL, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

price_yesterday = float(stock_data['Time Series (Daily)'][yesterday.strftime('%Y-%m-%d')]['4. close'])
price_before_yesterday = float(stock_data['Time Series (Daily)'][before_yesterday.strftime('%Y-%m-%d')]['4. close'])

variation = (price_yesterday - price_before_yesterday) / price_yesterday

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if abs(variation) > 0.05:
    news_parameters = {
        "q": COMPANY_NAME,
        "searchIn": "title,description",
        "from": yesterday.strftime('%Y-%m-%d'),
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_API_URL, params=news_parameters)
    news = news_response.json()['articles'][:3]

    # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    variation_mark = "🔺" if variation > 0 else "🔻"

    SMS_bodies = [
        f""""
        {STOCK}: {variation_mark}{math.ceil(variation * 100)}%
        Headline: {n['title']} 
        Brief: {n['description']}\n
        """ for n in news
    ]

    client = Client(account_sid, auth_token)

    for sms in SMS_bodies:
        message = client.messages.create(
            body=sms,
            from="+15017122661",
            to="+15558675318"
        )
        print(message.status)

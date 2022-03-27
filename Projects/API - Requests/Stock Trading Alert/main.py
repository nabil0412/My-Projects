from newsapi import NewsApiClient
import requests
import datetime
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY =  "STOCK API KEY"
NEWS_API_KEY = "NEWS API KEY"
CURRENT_DAY = datetime.date.today()
YESTERDAY = CURRENT_DAY - datetime.timedelta(days=1)
ACCOUNT_SID = "ACCOUNT SID"
AUTH_TOKEN = "AUTH TOKEN"
TWILIO_NUM = "TWILIO NUMBER"
PERSONAL_NUM = "PERSONAL NUMBER"


def GetNews():
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)

    all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                        sources='bbc-news,the-verge',
                                        domains='bbc.co.uk,techcrunch.com',
                                        from_param='2022-02-07',
                                        to='2022-03-07',
                                        language='en',
                                        sort_by='relevancy',
                                        )
    for i in range(3):
        article = all_articles["articles"][i]["title"]
        three_articles.append(article)                                 

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 4% or more between yesterday and the day before yesterday then print("Get News").


def DayClose(day):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}'
    r = requests.get(url)
    data = r.json()

    daily = data["Time Series (Daily)"] 
    today_data = daily[f"{day}"]

    close_today_data = today_data["4. close"]
    return close_today_data

today_data = float(DayClose(CURRENT_DAY))
yesterday_data = float(DayClose(YESTERDAY))
close_difference = today_data - yesterday_data

diff_per = int(abs(close_difference/yesterday_data) * 100)
if diff_per >= 4:
    print("Got News")
    three_articles = []
    GetNews()
    print(three_articles)
    if close_difference < 0 :
        client = Client(ACCOUNT_SID, AUTH_TOKEN) #,http_client=proxy_client)
        message = client.messages \
            .create(
            
            body=f"{COMPANY_NAME} is down {diff_per}% \n\nRecent articles: \n\n{three_articles[0]} \n\n{three_articles[1]} \n\n{three_articles[2]}",
            from_= TWILIO_NUM,
            to= PERSONAL_NUM
        )
        print(message.status)

    if close_difference > 0:
        client = Client(ACCOUNT_SID, AUTH_TOKEN) #,http_client=proxy_client)
        message = client.messages \
            .create(

            body=f"{COMPANY_NAME} is up {diff_per}% \n\nRecent articles: \n\n{three_articles[0]} \n\n{three_articles[1]} \n\n {three_articles[2]}",
            from_= TWILIO_NUM,
            to= PERSONAL_NUM
        )
        print(message.status)        
    

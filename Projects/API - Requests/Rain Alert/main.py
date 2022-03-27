import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "API_KEY"
#api_key = os.environ.get("OWM_API_KEY")
ACCOUNT_SID = "ACCOUNT_SID"
AUTH_TOKEN = "AUTH_TOKEN"
#auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": "41.878113",
    "lon": "-87.629799",
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        print(condition_code)
        will_rain = True

if will_rain:
    #proxy_client = TwilioHttpClient()
    #proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token) #,http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="TWILIO_NUM",
        to="PERSONAL_NUM"
    )
    print(message.status)

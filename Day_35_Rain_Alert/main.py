import requests
from twilio.rest import Client

api_key = "2bbb76622784f29b6dcfa95c1bed0ebd"
account_sid = "your_sid"
auth_token = "your_auth_token"

parameters = {
    "lat": 4.6766498,
    "lon": -74.069542,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_hourly = weather_data["hourly"][0:12]

conditions_id = [int(hour['weather'][0]['id']) for hour in weather_hourly]



if all(ele < 700 for ele in conditions_id):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from="+15017122661",
        to= "+15558675318"
    )
    print(message.status)

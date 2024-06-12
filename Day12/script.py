import time
import requests
from plyer import notification
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL_TEMPLATE = os.getenv("WEATHER_API_URL_TEMPLATE")

IP_INFO_API_KEY = os.getenv("IP_INFO_API_KEY")
IP_INFO_API_URL_TEMPLATE = os.getenv("IP_INFO_API_URL_TEMPLATE").replace("{IP_INFO_API_KEY}", "{api_key}")

def getMyCurrentLocation():
    try:
        res = requests.get(IP_INFO_API_URL_TEMPLATE.format(api_key=IP_INFO_API_KEY))
        res.raise_for_status() 
        return res.json().get('city')
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def fetchWeatherData(city):
    app_url = WEATHER_API_URL_TEMPLATE.format(api_key=WEATHER_API_KEY, city=city)
    try:
        res = requests.get(app_url)
        res.raise_for_status() 
        return res.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="D:/60DaysLearning/Day12/weather.ico",
        timeout=10
    )

def main():
    city = getMyCurrentLocation()
    if city:
        while True:
            weather_data = fetchWeatherData(city)
            if weather_data:
                location = weather_data['location']['name']
                temperature = weather_data['current']['temp_c']
                condition = weather_data['current']['condition']['text']
                notifyMe("Weather Update", f"Location: {location}\nTemperature: {temperature}°C\nCondition: {condition}")
            else:
                notifyMe("Weather Update", "Failed to fetch weather data.")
            time.sleep(30)  # Fetch weather data every 30 seconds
    else:
        notifyMe("Weather Update", "Failed to fetch city location.")

if __name__ == '__main__':
    main()

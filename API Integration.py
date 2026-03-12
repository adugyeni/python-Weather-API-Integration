import requests
import json

API_KEY = input('YOUR_API_KEY: ')  # Get one from OpenWeatherMap
CITY = input("Enter city: ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

def get_weather():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        data = response.json()
        print(f"\nWeather in {CITY}:")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Temp: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

get_weather()
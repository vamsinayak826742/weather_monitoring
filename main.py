import requests
import time
import datetime
from db import create_connection, create_table, insert_weather_summary

API_KEY = '3ea793a78717a7c3f0cea5a418c18697 '  # Replace with your OpenWeatherMap API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Connect to SQLite Database
conn = create_connection("weather_data.db")
create_table(conn)

def get_weather_data(city):
    response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}")
    return response.json()

def convert_k_to_c(temp_kelvin):
    return temp_kelvin - 273.15

def process_weather_data(data):
    city = data['name']
    date = datetime.datetime.fromtimestamp(data['dt']).date()
    temp = convert_k_to_c(data['main']['temp'])
    feels_like = convert_k_to_c(data['main']['feels_like'])
    weather_condition = data['weather'][0]['main']

    return (city, str(date), temp, temp, temp, weather_condition)  # avg, max, min are placeholders for now

while True:
    for city in CITIES:
        weather_data = get_weather_data(city)
        if weather_data.get('main'):
            summary = process_weather_data(weather_data)
            insert_weather_summary(conn, summary)
            print(f"Inserted data for {city}: {summary}")
    time.sleep(300)  # Wait for 5 minutes

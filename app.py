from flask import Flask, jsonify, render_template, request
import requests
import sqlite3
import time
import threading

API_KEY = "3ea793a78717a7c3f0cea5a418c18697"
CITIES = {
    "Delhi": 1273294,
    "Mumbai": 1275339,
    "Chennai": 1264527,
    "Bangalore": 1277333,
    "Kolkata": 1275004,
    "Hyderabad": 1269843
}

app = Flask(__name__)

# Temperature Conversion Functions
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Fetch data from OpenWeatherMap API
def fetch_weather_data():
    weather_data = {}
    for city, city_id in CITIES.items():
        params = {"id": city_id, "appid": API_KEY}
        response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params)
        if response.status_code == 200:
            data = response.json()
            weather_data[city] = {
                "main": data["weather"][0]["main"],
                "temp_c": kelvin_to_celsius(data["main"]["temp"]),
                "temp_f": kelvin_to_fahrenheit(data["main"]["temp"]),
                "feels_like_c": kelvin_to_celsius(data["main"]["feels_like"]),
                "feels_like_f": kelvin_to_fahrenheit(data["main"]["feels_like"]),
                "timestamp": data["dt"]
            }
    return weather_data

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect("database/weather_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                        city TEXT,
                        main TEXT,
                        temp_c REAL,
                        temp_f REAL,
                        feels_like_c REAL,
                        feels_like_f REAL,
                        timestamp INTEGER
                    )''')
    conn.commit()
    conn.close()

# Store data in database
def store_weather_data(weather_data):
    conn = sqlite3.connect("database/weather_data.db")
    cursor = conn.cursor()
    for city, data in weather_data.items():
        cursor.execute('''INSERT INTO weather (city, main, temp_c, temp_f, feels_like_c, feels_like_f, timestamp) 
                          VALUES (?, ?, ?, ?, ?, ?, ?)''',
                       (city, data["main"], data["temp_c"], data["temp_f"], data["feels_like_c"], data["feels_like_f"], data["timestamp"]))
    conn.commit()
    conn.close()

# Calculate aggregates for a selected city
@app.route('/api/aggregates', methods=['GET'])
def get_aggregates():
    city = request.args.get('city')
    conn = sqlite3.connect("database/weather_data.db")
    cursor = conn.cursor()

    # Fetch data for a specific city
    cursor.execute("SELECT temp_c FROM weather WHERE city=?", (city,))
    temps = [row[0] for row in cursor.fetchall()]
    
    if temps:
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        
        # Calculate the dominant weather condition
        cursor.execute("SELECT main, COUNT(main) FROM weather WHERE city=? GROUP BY main ORDER BY COUNT(main) DESC LIMIT 1", (city,))
        dominant_condition = cursor.fetchone()[0]
        
        aggregates = {
            "average_temp": avg_temp,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "dominant_condition": dominant_condition
        }
    else:
        aggregates = {}

    conn.close()
    return jsonify(aggregates)

# Serve main page
@app.route('/')
def index():
    return render_template('index.html')

# API to get current weather data
@app.route('/api/weather')
def weather():
    conn = sqlite3.connect("database/weather_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather ORDER BY timestamp DESC LIMIT 6")
    rows = cursor.fetchall()
    conn.close()

    weather_data = []
    for row in rows:
        weather_data.append({
            "city": row[0],
            "main": row[1],
            "temp_c": row[2],
            "temp_f": row[3],
            "feels_like_c": row[4],
            "feels_like_f": row[5],
            "timestamp": row[6]
        })
    return jsonify(weather_data)

# Schedule periodic updates every minute
def update_weather_data():
    while True:
        weather_data = fetch_weather_data()
        store_weather_data(weather_data)
        time.sleep(60)  # Fetch new data every 1 minute

if __name__ == "__main__":
    init_db()
    threading.Thread(target=update_weather_data, daemon=True).start()
    app.run(debug=True)

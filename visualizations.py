import sqlite3
import matplotlib.pyplot as plt

def fetch_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT date, avg_temp, max_temp, min_temp FROM weather;")
    return cursor.fetchall()

def plot_weather_summary(data):
    dates = [entry[0] for entry in data]
    avg_temps = [entry[1] for entry in data]
    max_temps = [entry[2] for entry in data]
    min_temps = [entry[3] for entry in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, avg_temps, label='Avg Temp (°C)', color='blue', marker='o')
    plt.plot(dates, max_temps, label='Max Temp (°C)', color='red', marker='o')
    plt.plot(dates, min_temps, label='Min Temp (°C)', color='green', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Weather Summary')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    conn = sqlite3.connect("weather_data.db")
    data = fetch_data(conn)
    plot_weather_summary(data)

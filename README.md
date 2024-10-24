
# Real-Time Weather Monitoring System with Rollups and Aggregates

## Objective
This project is a real-time weather monitoring dashboard built using Python, Flask, HTML/CSS, and JavaScript. It fetches live weather data for six major Indian cities (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad) from the OpenWeatherMap API and displays it on a dynamic web page, which updates every minute. The dashboard includes interactive visualizations such as bar charts, line charts, and pie charts to visualize current temperatures and weather conditions. It also provides daily weather summaries, user-configurable alerting thresholds, and options to convert temperatures between Celsius, Fahrenheit, and Kelvin

## Features
- **Real-time weather data retrieval** from the OpenWeatherMap API for major Indian cities.
- **Temperature conversion** from Kelvin to Celsius (or Fahrenheit, based on user preference).
- **Daily rollups and aggregates**, including:
  - Average, maximum, and minimum temperatures.
  - Dominant weather condition of the day.
- **Alerting system** for specific weather thresholds (e.g., high temperatures, specific weather conditions).
- **Data storage** to persist daily weather summaries.
- **Visualizations** for daily summaries, historical trends, and alerting.


## Project Structure

```
weather_monitoring/
├── static
│   ├── css
│   │   └── style.css              # Contains all the styles for the web dashboard
│   ├── js
│   │   └── script.js              # Handles dynamic chart rendering and data fetching
│
├── templates
│   └── index.html                 # The main HTML file for the dashboard
│
├── app.py                         # The main Flask application that serves the web page and fetches weather data
├── README.md                      # Project documentation
├── requirements.txt               # List of Python dependencies (Flask, requests, etc.)
└── .gitignore                     # Ignore file for Git

```

## Prerequisites

Ensure that the following are installed on your system:
- **Python 3.13**
- **pip (Python Package Installer)**

You will also need to sign up for an **API Key** from [OpenWeatherMap](https://openweathermap.org/).

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/vamsinayak826742/weather_monitoring.git
cd weather_monitoring
```
### 2. Create a Project Directory
Open a terminal or command prompt and create a new directory for your project:
bash
```
mkdir weather-dashboard
cd weather-dashboard
```

### 3. Install Dependencies
Here, requirements.txt file sqlite3 is commented if you want to install sqlite3 you can uncomment it and use.
```bash
pip install -r requirements.txt
```

### 4. Set Up the API Key
Obtain an API key from OpenWeatherMap and add it to your `config.py` file (see [Configuration](#configuration)).
my API key=3ea793a78717a7c3f0cea5a418c18697 

## Running the Project

Run the main script to start fetching weather data and processing it in real time:
```bash
python app.py
```


You can access the dashboard at `http://127.0.0.1:5000/`.

## Configuration

The project configuration is handled in `config.py`. Update the following variables:
```python
# config.py
API_KEY = "your_openweathermap_api_key_here"
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]  # List of cities to monitor
FETCH_INTERVAL = 300  # Weather data fetch interval in seconds (5 minutes by default)
TEMP_THRESHOLD = 35  # Temperature alert threshold (in Celsius)
```

## Usage

### 1. Weather Data Fetching
The system will automatically fetch weather data for the configured cities at the specified interval. It will log the weather information in real-time and compute daily rollups.

### 2. Temperature Conversion
All temperatures are converted from Kelvin to Celsius by default. You can change this behavior based on user preferences.

### 3. Daily Summaries
The system calculates daily aggregates for each city, including:
- Average temperature
- Maximum temperature
- Minimum temperature
- Dominant weather condition

The daily summary is stored in an SQLite database (`data/weather.db`).

### 4. Alerts
You can configure temperature or weather condition thresholds in `config.py`. Alerts will be triggered when a threshold is breached. Alerts can be displayed on the console or implemented to send notifications via email (not implemented but can be extended).

## API Key

Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your free API key. Replace the placeholder `API_KEY` in `config.py` with your actual key.


### Manual Testing
1. **Simulate weather updates** by running the main script for a few minutes.
2. **Verify temperature conversions** and check if the logs display accurate values.
3. **Check daily rollups** after 24 hours (or simulate shorter intervals for testing).
4. **Configure alert thresholds** and verify that alerts are triggered appropriately.

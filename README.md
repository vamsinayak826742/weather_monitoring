
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


## Output

# Real-Time Weather Monitoring Dashboard

#### Dynamic Weather Data Table
The Dynamic Weather Data Table is essential for displaying real-time weather data, updated every minute to reflect the latest conditions. The table includes the following key columns:

- **City**: Displays the name of the city for which the weather data is being reported.
- **Main Condition**: Indicates the primary weather condition (e.g., Clear, Rain, Clouds) affecting the city.
- **Temperature**: Shows the current temperature in the selected unit (Celsius, Fahrenheit, or Kelvin) based on user preference.
- **Feels Like**: Represents the perceived temperature, which takes into account factors like humidity and wind speed, providing a more accurate reflection of how the weather feels to individuals.
- **Time (Unix Timestamp)**: Displays the last updated time of the weather data in Unix timestamp format, giving context on when the information was last fetched.

#### Aggregate Data Table
The Aggregate Data Table provides key statistics about the weather data collected for a specific city, allowing users to analyze trends and patterns over time. It includes the following data representation:

- **Average Temperature**: Displays the average temperature over a specified period, giving insight into typical weather conditions.
- **Maximum Temperature**: Indicates the highest temperature recorded, which helps identify extreme weather events.
- **Minimum Temperature**: Shows the lowest temperature, providing context for colder weather conditions.
- **Dominant Condition**: Lists the most frequently occurring weather condition, summarizing the overall weather pattern for the city.

![Screenshot (803)](https://github.com/user-attachments/assets/69a95b78-d2fb-4c7d-b17e-6266d527e159)


## 1. Bar Chart (Current Temperature by City)

**Purpose:** This chart displays the current temperatures of various cities in a visual format, making it easy to compare temperatures across different locations.
**Data Representation:**
**X-axis**: Represents different cities (e.g., Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
**Y-axis**: Represents the temperature in degrees Celsius.
**Bars**: Each bar’s height corresponds to the current temperature for each city. The color of the bars varies based on temperature thresholds:
**Red**: Indicates high temperatures (above 35°C).
**Yellow**: Represents moderate temperatures (between 25°C and 35°C).
**Blue**: Indicates cooler temperatures (below 25°C).
**Insights**: This visualization helps users quickly identify which city is experiencing the hottest or coldest weather at a glance. It can be particularly useful for making decisions based on current weather conditions.

![Screenshot (804)](https://github.com/user-attachments/assets/64048365-0269-4de2-91f7-d092c00385ef)

## 2.Line Chart (Temperature Trends)

**Purpose:** The line chart visualizes the temperature trends over a specified time, showcasing how the temperatures have changed.
**Data Representation:**
**X-axis:** Represents time intervals (e.g., hours or days).
**Y-axis:** Represents temperature in degrees Celsius.
**Line:** A continuous line connects data points representing the temperatures at different times, allowing users to see trends (increasing, decreasing, or stable temperatures).
**Insights:** Users can identify patterns, such as daily temperature fluctuations, sudden temperature spikes, or drops, which can inform them about the overall weather trend in the selected cities.

![Screenshot (805)](https://github.com/user-attachments/assets/835b2ddd-c93b-40ba-b770-6bb072050e72)

## 3. Pie Chart (Weather Conditions Distribution)

**Purpose:** This chart displays the distribution of different weather conditions (e.g., clear, rain, clouds, thunderstorms) across the monitored cities.
**Data Representation:**
Each segment of the pie represents a different weather condition.
The size of each segment is proportional to the number of cities experiencing that particular weather condition.
**Color Coding:** Each weather condition is represented by a distinct color, making it easy to differentiate between them.
**Insights:** This visualization gives a quick overview of the prevalent weather conditions across the cities. For instance, a larger segment for “Rain” may indicate a rainy season or severe weather affecting multiple locations.


![Screenshot 2024-10-24 125756](https://github.com/user-attachments/assets/3b80977d-d9a4-46c6-93f6-dca0a5f96c45)


## Alerts Section

**Purpose:** The alerts section provides real-time notifications based on specific weather criteria, such as temperature thresholds.
**Data Representation:**
  * Alerts are displayed prominently when conditions exceed defined thresholds (e.g., temperature above 35°C).
  * Alerts are often color-coded for visibility, such as red for urgent conditions.
**Insights**: This feature is crucial for timely warnings about extreme weather that could impact safety, allowing users to take necessary precautions.

## Conclusion

  Each of these visualizations and data representations plays a vital role in delivering meaningful insights about the weather. Together, they create an interactive and informative dashboard that enables users to understand current conditions, track trends, and respond effectively to changing weather scenarios. The combination of graphical and tabular formats caters to different preferences for data consumption, enhancing user experience and engagement with the weather monitoring system.




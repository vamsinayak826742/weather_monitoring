
# Real-Time Weather Monitoring System with Rollups and Aggregates

## Objective
This project is a **Real-Time Data Processing System** designed to monitor weather conditions and provide summarized insights using **rollups** and **aggregates**. The system retrieves weather data from the **OpenWeatherMap API** and supports configurable alert thresholds and daily weather summaries.

## Features
- **Real-time weather data retrieval** from the OpenWeatherMap API for major Indian cities.
- **Temperature conversion** from Kelvin to Celsius (or Fahrenheit, based on user preference).
- **Daily rollups and aggregates**, including:
  - Average, maximum, and minimum temperatures.
  - Dominant weather condition of the day.
- **Alerting system** for specific weather thresholds (e.g., high temperatures, specific weather conditions).
- **Data storage** to persist daily weather summaries.
- **Visualizations** for daily summaries, historical trends, and alerting.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Project](#running-the-project)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [API Key](#api-key)
8. [Testing](#testing)


## Project Structure

```
weather_monitoring/
│
├── venv/                   # Virtual environment
├── data/                   # Directory for storing data (e.g., SQLite DB)
├── main.py                 # Main entry point of the application
├── utils.py                # Utility functions for weather data processing
├── weather_alerts.py       # Module to manage alerts based on user-defined thresholds
├── visualization.py        # Visualization functions using Dash
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── config.py               # Configuration for API and settings
```

## Prerequisites

Ensure that the following are installed on your system:
- **Python 3.10+**
- **Virtual Environment (venv)**
- **pip (Python Package Installer)**

You will also need to sign up for an **API Key** from [OpenWeatherMap](https://openweathermap.org/).

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/vamsinayak826742/weather_monitoring.git
cd weather_monitoring
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Set Up the API Key
Obtain an API key from OpenWeatherMap and add it to your `config.py` file (see [Configuration](#configuration)).
my API key=3ea793a78717a7c3f0cea5a418c18697 

## Running the Project

Run the main script to start fetching weather data and processing it in real time:
```bash
python main.py
```

### Running the Dashboard (Optional)
To visualize the daily summaries and alerts, run the dashboard:
```bash
python visualization.py
```

You can access the dashboard at `http://localhost:8050`.

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

## Testing

### Unit Tests
You can simulate API calls and test the system's behavior under different scenarios using the provided test cases in `tests/`.

To run the tests:
```bash
pytest tests/
```

### Manual Testing

1. **Simulate weather updates** by running the main script for a few minutes.
2. **Verify temperature conversions** and check if the logs display accurate values.
3. **Check daily rollups** after 24 hours (or simulate shorter intervals for testing).
4. **Configure alert thresholds** and verify that alerts are triggered appropriately.


async function fetchWeatherData() {
    const response = await fetch('/api/weather');
    const weatherData = await response.json();
    const table = document.getElementById('weather-table');
    const unit = document.getElementById('unit').value;
    table.innerHTML = `
        <tr>
            <th>City</th>
            <th>Main</th>
            <th>Temperature</th>
            <th>Feels Like</th>
            <th>Time (Unix Timestamp)</th>
        </tr>
    `;
    
    const temperatures = []; // Store temperatures for the bar chart
    weatherData.forEach(data => {
        let temp = data.temp_c;
        let feelsLike = data.feels_like_c;
        
        if (unit === 'fahrenheit') {
            temp = data.temp_f;
            feelsLike = data.feels_like_f;
        } else if (unit === 'kelvin') {
            temp = data.temp_c + 273.15;
            feelsLike = data.feels_like_c + 273.15;
        }

        temperatures.push(temp); // Add temperature to the array

        const row = `
            <tr>
                <td>${data.city}</td>
                <td>${data.main}</td>
                <td>${temp.toFixed(2)}</td>
                <td>${feelsLike.toFixed(2)}</td>
                <td>${data.timestamp}</td>
            </tr>
        `;
        table.innerHTML += row;
    });

    renderBarChart(weatherData); // Call the function to render the bar chart
}

async function fetchAggregates(city) {
    const response = await fetch(`/api/aggregates?city=${city}`);
    const aggregates = await response.json();
    const aggContainer = document.getElementById('aggregates');
    const aggTable = document.getElementById('aggregate-table');

    aggContainer.innerHTML = `<h3>Aggregates for ${city}</h3>`;
    aggTable.innerHTML = `
        <tr>
            <th style="background-color: #28a745; color: white;">Average Temperature (°C)</th>
            <th style="background-color: #dc3545; color: white;">Maximum Temperature (°C)</th>
            <th style="background-color: #ffc107; color: black;">Minimum Temperature (°C)</th>
            <th style="background-color: #007bff; color: white;">Dominant Condition</th>
        </tr>
        <tr>
            <td style="background-color: #d4edda;">${aggregates.average_temp.toFixed(2)}</td>
            <td style="background-color: #f8d7da;">${aggregates.max_temp.toFixed(2)}</td>
            <td style="background-color: #ffeeba;">${aggregates.min_temp.toFixed(2)}</td>
            <td style="background-color: #cce5ff;">${aggregates.dominant_condition}</td>
        </tr>
    `;
    aggTable.style.display = 'table'; // Show the aggregate table
}


// Visualization with updated colors
function renderCharts() {
    const lineCtx = document.getElementById('tempLineChart').getContext('2d');
    const tempLineChart = new Chart(lineCtx, {
        type: 'line',
        data: {
            labels: ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad'],
            datasets: [{
                label: 'Temperature (°C)',
                data: [29, 32, 31, 28, 30, 29],
                borderColor: 'rgba(54, 162, 235, 1)',
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                fill: true
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    const pieCtx = document.getElementById('conditionPieChart').getContext('2d');
    const conditionPieChart = new Chart(pieCtx, {
        type: 'pie',
        data: {
            labels: ['Clear', 'Rain', 'Clouds', 'Thunderstorm'],
            datasets: [{
                data: [10, 15, 8, 5],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)',
                    'rgba(75, 192, 192, 0.6)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)'
                ],
                borderWidth: 1
            }]
        }
    });
}

async function checkAlerts(currentTemp) {
    const alertContainer = document.getElementById('alert-container');
    if (currentTemp > 35) {
        alertContainer.innerHTML = '<div class="alert">Alert: Temperature exceeds 35°C!</div>';
    } else {
        alertContainer.innerHTML = ''; // Clear alert if no longer applicable
    }
}

// Function to render the bar chart
async function renderBarChart(weatherData) {
    const ctx = document.getElementById('countryBarChart').getContext('2d');

    const cities = [];
    const temperatures = [];

    weatherData.forEach(data => {
        cities.push(data.city); // Get the city name
        temperatures.push(data.temp_c); // Get the temperature in Celsius
    });

    const colors = temperatures.map(temp => {
        // Change color based on temperature ranges
        if (temp > 35) return 'rgba(255, 99, 132, 0.6)'; // Red for high temperatures
        if (temp > 25) return 'rgba(255, 206, 86, 0.6)'; // Yellow for moderate temperatures
        return 'rgba(54, 162, 235, 0.6)'; // Blue for low temperatures
    });

    const countryBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: cities,
            datasets: [{
                label: 'Current Temperature by City (°C)',
                data: temperatures,
                backgroundColor: colors, // Different colors based on temperature
                borderColor: 'rgba(0, 0, 0, 0.7)', // Black border
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Temperature (°C)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Cities'
                    }
                }
            }
        }
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    fetchWeatherData();
    renderCharts();
    setInterval(fetchWeatherData, 60000);  // Update weather data every 1 minute
});

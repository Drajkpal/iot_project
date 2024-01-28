from faker import Faker
import random
from datetime import datetime, timedelta

# Create a Faker instance
fake = Faker()

# Define a function to generate weather data
def generate_weather_data(start_date, end_date):
    weather_data = [['Temprature','Humidity','Rainfall','wind_speed','light_intensity','timestamp']]
    delta = timedelta(hours=1)
    while start_date <= end_date:
        data = [
            round(random.uniform(-5, 32), 2),  # Temperature in Celsius
            round(random.uniform(0, 100), 2),  # Humidity in %
            round(random.uniform(0, 200), 2),  # Rainfall in mm
            round(random.uniform(0, 32.7), 2),  # Wind speed in m/s
            round(random.uniform(0, 100000), 2),  # Light intensity in lux
            start_date  # Timestamp of the data
        ]
        weather_data.append(data)
        start_date += delta
    return weather_data

# Generate weather data for every hour from November 1 to November 30
start_date = datetime(2023, 11, 1)
end_date = datetime(2023, 11, 30, 23, 59, 59)
weather_data = generate_weather_data(start_date, end_date)

# Print the data in a structured format
for data in weather_data:
    print(','.join(map(str, data)))
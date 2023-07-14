import csv
import random

# Define cities in US and Europe
us_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
eu_cities = ['London', 'Paris', 'Berlin', 'Madrid', 'Rome']

# Define range of temperatures and humidities
us_temperatures_range = (0, 110) # In Fahrenheit
eu_temperatures_range = (-20, 40) # In Celsius
humidity_range = (0, 100) # Percentage

data = []

# Add header
data.append(['City', 'Country', 'Day', 'Temperature', 'Humidity'])

# Generate data for US cities
for city in us_cities:
    for day in range(1, 31000):
        temperature = random.randint(*us_temperatures_range)
        humidity = random.randint(*humidity_range)
        data.append([city, 'US', day, temperature, humidity])

# Generate data for Europe cities
for city in eu_cities:
    for day in range(1, 31000):
        temperature = random.randint(*eu_temperatures_range)
        humidity = random.randint(*humidity_range)
        data.append([city, 'Europe', day, temperature, humidity])

# Write data to CSV file
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

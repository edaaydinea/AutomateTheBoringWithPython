#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = "49fcbb31bd21504ad782200cf27ac76f"

import json, requests, sys

# Get geolocation from command line
if len(sys.argv) < 2:
    print("Usage: getOpenWeather.py zip code, country code")
    sys.exit()

zip_code = sys.argv[1]
country_code = sys.argv[2]

url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={APPID}"
response = requests.get(url)
response.raise_for_status()

# Get latitude and longitude from response
location_data = json.loads(response.text)
lat = location_data["lat"]
lon = location_data["lon"]

# Get weather data from latitude and longitude
url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APPID}&units=metric"

response2 = requests.get(url2)
response2.raise_for_status()

weather_data = json.loads(response2.text)

# Print weather data
print(f"Current weather in {zip_code}, {country_code}:")
print(weather_data["weather"][0]["main"], " - ", weather_data["weather"][0]["description"] + " - " + str(weather_data["main"]["temp"]) + "°C")


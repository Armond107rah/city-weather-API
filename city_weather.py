import requests


API_Key = "ef36bb3162a4d8e7ee5599df86b91244"

# ask user for city name, country name
location = input("Enter your location: ")

LAT_LON_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&appid={API_Key}"

#using user's location get the lat, long

response = requests.get(LAT_LON_URL)
data = response.json()

lat = data[0]['lat']
lon = data[0]['lon']

print(lat, lon)

# using lat and long we will get the weather

WEATHER_URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API_Key}"
print(WEATHER_URL)


response = requests.get(WEATHER_URL)

data = response.json()

print("=============")
print(data)
print("=================")

description = data['current']['weather'][0]['description']

print(description)
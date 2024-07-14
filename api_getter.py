# Get weather data from the weather.gov API
# TODO: get data from the api

import requests

weather = requests.get("https://api.weather.gov/gridpoints/RAH/74,57/forecast")

forecast = weather.json()

for i in range(0, 14):
	print(forecast['properties']['periods'][i]['name'] + ":", forecast['properties']['periods'][i]['temperature'])


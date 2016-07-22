#! python3
# quickWeather.py - Prints the weather for a locationid by default for Astana.

import json, requests, sys

idlocation = '1526273'

# Download the JSON data from OpenWeatherMap.org's API
url ='http://api.openweathermap.org/data/2.5/forecast/city?id=%s&APPID=e1051e3a3ff0840d651e39e00bfb1040' % (idlocation)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.
w = weatherData['list']
print('Current weather in Astana')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

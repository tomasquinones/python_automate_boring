# Chapter 16 - Fetching Current Weather Data
# getOpenWeather.py - Prints the weather for a location from the command line.


import json, requests, sys

APPID = '159a3517f4e1564d5f76e7ac5f7b5e5d'

# Computer location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

# print(location)
# TODO: Download the JSON data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (location, APPID)

response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
print(response.text)


# Load JSON data into a Python Variable.
weatherData = json.loads(response.text)

    # Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
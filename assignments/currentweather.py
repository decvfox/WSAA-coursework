# currentweather.py
# prints out the current temperature on the console
#Author: Declan Fox

import requests
import json

url = 'https://api.open-meteo.com/v1/forecast?latitude=53.41&longitude=8&current=temperature_2m,wind_direction_10m'
response = requests.get(url, verify=False)
data = response.json()

'''
with open ("weather_dump.json", "w") as fp:
    json.dump(data, fp)
'''
current_temp = data["current"]["temperature_2m"]
wind_direction = data["current"]["wind_direction_10m"]
print(f'The current temp is: {current_temp}\N{DEGREE SIGN}C')
print(f'The current wind direction is: {wind_direction}\N{DEGREE SIGN}')
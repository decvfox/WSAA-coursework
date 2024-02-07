# flood.py
# prints out the current water level at Corofin bridge
# Here Clare in the station name refers to the river not the county.
# Author: Declan Fox
import requests
import json

url = 'https://waterlevel.ie/geojson/latest/'
response = requests.get(url, verify=False)
data = response.json()

# with open ("flood_dump.json", "w") as fp:
#    json.dump(data, fp)

features = data["features"]
for feature in features:
    station = feature["properties"]["station_name"]
    sensor = feature["properties"]["sensor_ref"]
    if station == "Corrofin  Clare " and sensor == "0001":
        level = feature["properties"]["value"]
        print(f'\nThe current water level at Corofin bridge is: {level}m\n')
        break


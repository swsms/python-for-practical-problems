import re

import requests

url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
response = requests.get(url)

if not response.ok:
    print(f'Cannot retrieve the html from {url}')

xml = str(response.content.decode('utf-8'))

fuel_stations = re.findall('k="amenity" v="fuel"', xml)

print(len(fuel_stations))

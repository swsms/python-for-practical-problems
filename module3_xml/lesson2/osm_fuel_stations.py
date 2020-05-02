import requests
import xmltodict


def is_fuel_station_tag(tag: str) -> bool:
    return ('@k' in tag
            and tag['@k'] == 'amenity'
            and tag['@v'] == 'fuel')


url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
response = requests.get(url)

if not response.ok:
    print(f'Cannot retrieve the html from {url}')

xml = response.content.decode('utf-8')
osm_xml = xmltodict.parse(xml)

fuel_stations_count = 0

for node in osm_xml['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, list):
            for tag in tags:
                if is_fuel_station_tag(tag):
                    fuel_stations_count += 1
        else:
            if is_fuel_station_tag(tags):
                fuel_stations_count += 1

print(fuel_stations_count)

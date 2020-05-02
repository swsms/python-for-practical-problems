import requests
import xmltodict

url = 'https://stepik.org/media/attachments/lesson/245571/map1.osm'
response = requests.get(url)

if not response.ok:
    print(f'Cannot retrieve the html from {url}')

xml = response.content.decode('utf-8')
parsed_xml = xmltodict.parse(xml)

print(parsed_xml['osm']['node'][100]['@id'])

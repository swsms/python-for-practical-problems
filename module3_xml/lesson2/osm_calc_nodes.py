import requests
import xmltodict

url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'
response = requests.get(url)

if not response.ok:
    print(f'Cannot retrieve the html from {url}')

xml = response.content.decode('utf-8')
osm_xml = xmltodict.parse(xml)

node_with_tag = 0
node_without_tag = 0

for node in osm_xml['osm']['node']:
    if 'tag' in node:
        node_with_tag += 1
    else:
        node_without_tag += 1

print(f'{node_with_tag} {node_without_tag}')

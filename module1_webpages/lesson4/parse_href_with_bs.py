import requests
from bs4 import BeautifulSoup

url = 'https://stepik.org/media/attachments/lesson/245130/6.html'
response = requests.get(url)

if not response.ok:
    print(f'Cannot retrieve the html from {url}')

html = response.content.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

for hyperlink in soup.find_all('a', href=True):
    print(hyperlink['href'])

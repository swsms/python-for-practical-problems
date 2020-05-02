import requests
from bs4 import BeautifulSoup

# ​​​​Python Web Scraping Using BeautifulSoup
# https://www.dataquest.io/blog/web-scraping-tutorial-python/
# BS documentations
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

url = 'http://dataquestio.github.io/web-scraping-pages/simple.html'
response = requests.get(url)

if not response.ok:
    print(f'Cannot retrieve the html from {url}')

html = response.content.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

[print(type(item)) for item in list(soup.children)]

print(soup.find('p').get_text())

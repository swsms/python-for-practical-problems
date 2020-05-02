from urllib.request import urlopen

from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245130/6.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', attrs={'class': 'wikitable sortable'})

count = 0
for tr in soup.find_all('tr'):
    count += 1
    for td in tr.find_all(['td', 'th']):
        count *= 2

print(count)

import requests
from bs4 import BeautifulSoup

url = 'https://stepik.org/media/attachments/lesson/209723/5.html'
response = requests.get(url)

if not response.ok:
    print(f'Cannot retrieve the html from {url}')

html = response.content.decode('utf-8')

# html5lib is used for non-valid html docs
soup = BeautifulSoup(html, 'html5lib')

numbers = (int(tag.get_text()) for tag in soup.find_all('td'))
print(sum(numbers))

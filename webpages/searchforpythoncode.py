import re
from collections import Counter
from urllib.request import urlopen

page_url = 'https://stepik.org/media/attachments/lesson/209719/2.html'

html = str(urlopen(page_url).read().decode('utf-8'))

strings = sorted(re.findall("<code>(.*?)</code>", html))
counter = Counter(strings)

print(counter)

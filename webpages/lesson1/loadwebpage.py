from urllib.request import urlopen

page_url = 'https://stepik.org/media/attachments/lesson/209717/1.html'

html = str(urlopen(page_url).read().decode('utf-8'))

print(html.count('C++'))
print(html.count('Python'))

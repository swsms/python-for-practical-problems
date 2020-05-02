from urllib.request import urlopen

url = 'https://ru.wikipedia.org/wiki/Python'
html = str(urlopen(url).read().decode('utf-8'))
offset = 9

pos = html.find('<a href=')
while pos != -1:
    posquote = html.find('"', pos + offset)
    href = html[pos + offset:posquote]
    print(href)
    pos = html.find('<a href=', pos + 1)

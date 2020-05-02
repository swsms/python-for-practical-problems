from urllib.request import urlopen

page_url = 'https://stepik.org/media/attachments/lesson/209717/1.html'

html = str(urlopen(page_url).read().decode('utf-8'))

characters = []
state = 0

for char in html:
    if char == '<':
        state = 1
    elif char == '>':
        state = 0
    elif state == 0:
        characters.append(char)

text = ''.join(characters)
print(text.count('C++'))

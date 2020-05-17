#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text1 = form.getfirst('TEXT_1', 'не задано')
text2 = form.getfirst('TEXT_2', 'не задано')

print('Content-type: text/html\n')
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print('<h1>Обработка данных форм!</h1>')
print(f'<p>TEXT_1: {text1}</p>')
print(f'<p>TEXT_2: {text2}</p>')

print("""</body>
        </html>""")

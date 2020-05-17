#!/usr/bin/env python3

print('Content-type: text/html')
print()
print('<html>')
print('<body>')
print('<table>')

for i in range(1, 11):
    print('<tr>')
    for j in range(1, 11):
        print(f'<td><a href=http://{i * j}.ru>{i * j}</a></td>')
    print('</tr>')

print('</table>')
print('</body>')
print('</html>')

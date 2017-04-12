# from: https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html#Quick%20Start

from bs4 import BeautifulSoup
import re, requests

# doc = ['<html><head><title>Page title</title></head>',
#        '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
#        '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
#        '</html>']
# soup = BeautifulSoup(''.join(doc))

# print(soup.prettify())

# print(soup.contents[0].name)
# head = soup.contents[0].contents[0]
# print(head.parent.name)

# print(head.next)
# print(head.nextSibling.name)
# print(head.nextSibling.contents[0])
# print(head.nextSibling.contents[0].nextSibling)

r = requests.get('https://icc-ccs.org/index.php/piracy-reporting-centre/live-piracy-report')
print('Status code: ' + str(r.status_code))

soup = BeautifulSoup(r.text, 'html.parser')

for incident in soup('td', width='90%'):
	where, linebreak, what = incident.contents[:3]
	print(where.strip())
	print(what.strip())
	print('\n')

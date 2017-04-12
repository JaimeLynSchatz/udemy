# webscraping and beautiful soup 4

import bs4, requests

data = open('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?ie=UTF8&qid=1491939561&sr=8-1&keywords=automate+the+boring+stuff+with+python').read()
diagnose(data)

# def getAmazonPrice(productUrl):
# 	res = requests.get(productUrl)
# 	res.raise_for_status()

# 	soup = bs4.BeautifulSoup(res.text, 'html.parser')

# 	elems = soup.selector('#quick-start > p:nth-child(6)')
# 	return elems[0].text.strip()
# 	#return elems[0].text.strip()

# price = getAmazonPrice('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
# print('the price is ' + str(price))
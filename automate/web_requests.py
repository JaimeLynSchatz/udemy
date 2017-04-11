import requests

rjURL = 'https://automatetheboringstuff.com/files/rj.txt'

res = requests.get(rjURL)
res.status_code
len(res.text)
print(res.text[:500])

res.raise_for_status()
# badRes = requests.get('https://automatetheboringstuff.com/fakefiledonotexist')
# you can wrap this in a try catch
# badRes.raise_for_status()


playFile = open('RomeoAndJuliet.txt', 'wb')
# wb is write binary
# bit.ly/unipain
for chunk in res.iter_content(100000):
	playFile.write(chunk)
playFile.close()
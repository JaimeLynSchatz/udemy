# Text Files

import shelve

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['list', 'of', 'data', 'that', 'you', 'want', 'to', 'keep']

list(shelfFile.keys())
list(shelfFile.values())

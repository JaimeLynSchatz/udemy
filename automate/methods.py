# Methods

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')
spam.append('adding this')
spam.remove('adding this')
spam.insert(1, 'adding it back')

import copy
spam = ['A', 'B', 'C']
cheese = copy.deepcopy(spam)
# now it's not just a reference - it's a whole new list

spam = ['apples',
        'oranges',
        'bananas',
        'cats']
print('Four score and seven ' + \
	spam[-1] + ' ago')
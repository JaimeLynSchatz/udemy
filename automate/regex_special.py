import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

phoneRegex.findall('Big ol' piece of text) with lots of phone numbers - use your imagination')

# findall returns a list of strings, or if there are two or more groups, a list of tuples holding the values

\d - any digit
\D - any character not a digit
\w - Any letter, digit or underscore
\W - Any character that's not a letter, digit or underscore
\s - any white space
\S - any non-white space

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtledoves, and 1 partridge in a pear tree!'

xmasRegex = re.compile(r'\d+\s\w+')

regexObj = re.compile(r'[]')

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('Robocop eats babyfood')

doubleVowel = re.compile(r'[aeiouAEIOU]{2}')
consonants = re.compile(r'[^aeiouAEIOU]')

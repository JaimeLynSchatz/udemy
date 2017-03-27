# more string methods

spam = 'Hello world!'
print(spam.upper()) # does not convert in place, returns an uppercase version
print(spam)

print(spam.lower())

print(spam)
print(spam + 'is lowercase?' + spam.islower())
print(spam + 'is uppercase?' + spam.isupper())

print('What if I run it through upper first?')
print('Hello'.upper().isupper())

# other fun ones to try
isalpha()
isalnum()
isdecimal()
isspace()
istitle() # title case

print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))

replace()

# pyperclip
import pyperclip
pyperclip.copy()
pyperclip.paste()


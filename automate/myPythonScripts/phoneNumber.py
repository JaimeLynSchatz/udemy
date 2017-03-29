# Regular Expressions for the win!

import re

message = 'Call me at 215-222-2345 or at 345-678-1234 tomorrow!'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

print(phoneNumRegex.findall(message))
print(mo.group())

# Without Regular Expressions

def isPhoneNumber(text):
  if len(text) != 12:
    return False # not phone number-sized
  for i in range(0, 3):
    if not text[i].isdecimal():
      return False # no area code
  if text[3] != '-':
    return False # missing dash
  for i in range(4, 7):
    if not text[i].isdecimal():
      return False # not numbers
  if text[7] != '-':
  	return False # missing dash
  for i in range(8, 12):
  	if not text[i].isdecimal():
  		return False # not numbers
  return True

# print(isPhoneNumber('hello'))
# print(isPhoneNumber('425-555-1212'))


foundNumnber = False
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('Phone number found: ' + chunk)
		foundNumber = True
if not foundNumber:
	print('Count not find any phone numbers.')
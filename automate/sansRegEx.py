# Regular Expressions for the win!

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
  return True

print(isPhoneNumber('hello'))
print(isPhoneNumber('425-555-1212'))


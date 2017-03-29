import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 425-555-1212')
print(mo.group())
#print(mo.group(1))
#print(mo.group(2))
#print(mo.group(3))

phoneNumRegex = re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
mo = batRegex.search('Batmotorcycle lost a wheel')
print(mo == None)

# ? matches zero or 1
# * matches zero or more times
# + matches at least 1

# If you're searching for one of those symbols, use the \ to escape

haRegex = re.compile(r'(Ha){3}')

newPhoneRegex = re.compile(r'\(?(\d{3}\)?-)?(\d){3}-(\d){4}')


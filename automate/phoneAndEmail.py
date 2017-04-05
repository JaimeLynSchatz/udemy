#! python

import re, pyperclip

# Create a regex for phone numbers

# 425-351-4601, (425) 351-4601, 351-4601, 351-4601 ext 12345, 351-4601 ext 12345, 351-4601 x12345
phoneRegex = re.compile(r'''
(  # findall does something funny with groups -- put this all in one group
((\d\d\d)|(\(\d\d\d\)))?    # area code optional
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|x)         	# extension word part optional
 (\d{2,5}))?	
 )				# extention number part optional
''', re.VERBOSE)



# TODO: Create a regex for email addresses
# some.+_thing@something.com|edu|net
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+				# name part 
@							# @ symbol
[a-zA-Z0-9_.+]+				# domain name part
''', re.VERBOSE)

# TODO: Get the text off the clipboard
textToParse = pyperclip.paste() # be certain to copy something to clipbaord first!

# TODO: Extract the email/phone from thie text
extractedPhone = phoneRegex.findall(textToParse)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
	allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)

extractedEmail = emailRegex.findall(textToParse)
print(extractedEmail)
# TODO: Copy the extracted email/phone to the clipboard



results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
print(results)
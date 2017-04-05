# .sub()

namesRegex = re.compile(r'Agent (\w)\w*') # will match a group with the first letter of the Agent's name

namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.') # the \1 says to use the group that matches the regex token followed by stars

# re.VERBOSE
re.compile(r'''
\d\d\d     #  area code
-          #  first dash
\d\d\d     #  first group of digites
-          #  second dash
\d\d\d\d)  #  last 4 digits
''', re.VERBOSE | re.DOTALL | re.VERBOSE)  # bitwise operator to include multiple arguments to the compile function




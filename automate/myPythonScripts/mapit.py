# webbrowser module
#! python3

import webbrowser, sys, pyperclip

# command line arguments will be stored here sys.argv

# sys.argv #[ 'mapit.py', '870', 'Valencia', 'St.']

if len(sys.argv) > 1: 
	address = ' '.join(sys.argv[1:])
else: # assume the user wants to use what's on the clipboard
	address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)

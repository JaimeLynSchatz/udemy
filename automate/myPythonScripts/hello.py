# running out of command line

#Shebang line

#! python3
import sys
print('Hello World!')

if len(sys.argv) > 0:
	print('what did you say?')
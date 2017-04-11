# logging

import logging

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# logging.disable(logging.CRITICAL)
# DEBUG, INFO, WARNING, ERROR, CRITICAL

logging.debug('Start of factorial')

def factorial(n):
	logging.debug('in Factorial')
	total = 1
	for i in range(1, n + 1):
		total *= i
		logging.debug('i is %s, total is %s' % (i, total))
	return total

print(factorial(5))
logging.debug('total returned is ' + str(factorial(5)))

logging.debug('End of program')
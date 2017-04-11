# Debugging

"""

*******************
*                 *
*                 *
*                 *
*******************
"""

def boxPrint(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('Symbol must be a length of 1')
	if (width < 2) or (height < 2):
		raise Exception('"Width" and "Height" must be at least 2')
	print(symbol * width)

	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)
	print(symbol * width)

boxPrint('^', 10, 4)
boxPrint('%', 6, 20)
boxPrint('@', 1, 6)


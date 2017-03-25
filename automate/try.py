def div42by(divideBy):
  try:
    return 42 / divideBy
  except ZeroDivisionError:
  	print('Error: You tried to divide by zero')

print(div42by(2))
print(div42by(0))
print(div42by(5))

print('How many cats do you own?')
numCats = input()
try:
	if int(numCats) < 0:
		print('How do you have negative cats?')
	elif int(numCats) >= 4:
		print('That is a lot of cats.')
	else:
		print('That is not so many cats.')
except ValueError:
	print('You did not enter a number')
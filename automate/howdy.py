def hello(name):
  print('Howdy' + name + '!')
  print('Howdy!!')
  print('Hello there!')

hello('Alice')
hello('Bob')
hello('Peter')

def plusOne(number):
	return number + 1

newNumber = plusOne(4)
print(newNumber)
newNumber = plusOne(10)
print(newNumber)

print('cat', 'dog', 'mouse')
print('cat', 'dog', 'mouse', sep=' ------ ')
print('cat', end='')
print('dog', 'mouse')
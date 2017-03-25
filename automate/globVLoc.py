spam = 42 # global variable

def eggs():
  spam = 'forty two' # local variable
  print(spam)

eggs()
print(spam)

def eggs(someParameter):
  someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)  # you are sending a reference, not the value
print(spam)


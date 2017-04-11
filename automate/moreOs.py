import os

open(os.path.join(os.getcwd(), 'hello.txt')
  
>>> helloFile = open(os.path.join(os.getcwd(), 'hello.txt')
... )
>>> fileContents = helloFile.read()
>>> helloFile.close()
>>> fileContents
'Hello world!'
>>> helloFile = open(os.path.join(os.getcwd(), 'hello.txt')
... )
>>> helloFile.readlines()
['Hello world!']


helloFile = open(os.path.join(os.getcwd(), 'hello2.txt'), 'w')
# opening a file for reading
# ,w is for overwriting
# ,a is for appending

helloFile.write('Hello!!!!')
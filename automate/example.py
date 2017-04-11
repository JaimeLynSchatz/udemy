import os

for filename in os.listdir():
  if filename.endswith('.txt'):
    #os.unlink(filename)
    print(filename)  # dry run to test what you're doing
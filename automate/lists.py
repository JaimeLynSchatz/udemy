spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print('The ' + spam[0][0] + ' is afraid of the ' + spam[0][-1])

spam[1:3] # a slice, starts at first number, goes up to the second

supplies = ['pens', 'staplers', 'flamethrowers', 'paper']

for i in range(len(supplies)):
  print('Index ' + str(i) + ' ' + supplies[i])

cat = ['fat', 'orange', 'loud']
size, color, disposition = 'skinny', 'blank', 'quiet'
a = 'AAA'
b = 'BBB'
a, b = b, a

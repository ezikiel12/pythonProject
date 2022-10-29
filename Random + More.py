import random
ranList = []

for x in range (10):
    ranList.insert(x, random.randrange(5000))

print(ranList)
print('The maximum value in the list is:', max(ranList))

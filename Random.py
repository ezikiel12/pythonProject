import random

range1 = 1000
range2 = 10000
nums = []
values = range1
count = 0

for x in range((range2 + 1)-range1):
    nums.insert(count , values)
    count = count + 1
    values = values + 1

print(nums)
print ("Random number from range:" , random.choice(nums))
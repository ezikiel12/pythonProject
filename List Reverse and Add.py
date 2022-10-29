import random


lis = []
for x in range(10):
    lis.insert(x,random.randrange(100))
print("Original list:", lis)

def rever(nums):
    nums.reverse()
    print("Reversed list:", lis)
    print("Sum of all items in list:", sum(nums))

rever(lis)




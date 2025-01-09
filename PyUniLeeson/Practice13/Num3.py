import math
file = open('num3text.txt')
fr = file.readlines()
file.close()

print(fr)

nums = []
for s in fr:
    nums.append(int(s[0]))

print(nums)

print(math.prod(nums))
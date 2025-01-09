#3
#Максимально возможным натуральным числом взято четырехзначное число
nums_num = int(input('Enter numbers quantity: '))
from random import randint
nums_of_nums = []
evens_num = []
for j in range(0,nums_num):
    numbers = []
    for i in range(0,4):
        numbers.append(randint(0,9))
    nums_of_nums.append(numbers)
print(nums_of_nums)
for k in range(0,nums_num):
    for l in range(0, 4):
        if nums_of_nums[k][l]%2==0:
            evens_num.append(1)
print(sum(evens_num))
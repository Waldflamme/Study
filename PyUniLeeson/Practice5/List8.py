num = int(input('Enter number of elements: '))
numk = int(input('Enter number k: '))
from random import randint
numbers = []
for i in range(0,num):
    numbers.append(randint(-999,999))
new_numbers = []
for j in range(0,len(numbers)):
    if numbers[j]<numk:
        new_numbers.append(numbers[j])
print(numbers)
new_numbers.sort()
print(new_numbers)
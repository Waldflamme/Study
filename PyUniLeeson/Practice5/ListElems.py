num = int(input('Enter number of elements: '))
num2 = int(input('Enter number K: '))
num3 = int(input('Enter number L: '))
from random import randint
numbers = []
for i in range(0,num):
    numbers.append(randint(-999,999))
print(numbers)
print(numbers[:num2-1:]+numbers[num3::])
print(sum(numbers[:num2-1:]+numbers[num3::]))
num = int(input('Enter number of elements: '))
from random import randint
numbers = []
for i in range(0,num):
    numbers.append(randint(-999,999))
K = numbers.index(max(numbers))
L = numbers.index(min(numbers))
print(numbers)
print(K)
print(L)
if numbers[K]>numbers[L]:
    print(sum(numbers[numbers[L]:numbers[K]+1:]))
elif numbers[K]<numbers[L]:
    print(sum(numbers[numbers[K]:numbers[L]+1:]))
from random import randint
def sum_num(n):
    return n//100+n%100//10+n%10
num = int(input('Enter number of elements: '))
lst = []
for i in range(num):
    lst.append(randint(100,999))
print(lst)
print(sorted(lst, key=sum_num))
from random import randint
def isprime(l):
    d = 2
    while l%d !=0:
        d += 1
    return d == l
m = int(input('Enter number of columns: '))
n = int(input('Enter number of strings: '))
a = []
b = []
for i in range(n):
    for j in range(m):
        b.append(randint(0,999))
    a.append(list(b))
    b.clear()
for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()
for i in range(n):
    print(sum(a[i]))
    if isprime(sum(a[i])):
        print(i)
    else:
        print()

from random import randint
n = int(input('Enter array rank: '))

def Transp(lst):
    ls = []
    for i in range(n):
        lt = []
        for j in range(n):
            lt.append(lst[j][i])
        ls.append(lt)
    print()
    for i in range(n):
        for j in range(n):
            print(ls[i][j], end=' ')
        print()
a = []
b = []
for i in range(n):
    for j in range(n):
        b.append(randint(0,999))
    a.append(list(b))
    b.clear()
for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()
print()
Transp(a)
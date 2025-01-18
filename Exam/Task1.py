from random import randint
m = int(input('Enter number of columns: '))
n = int(input('Enter number of strings: '))


def MaxLoad(lst):
    max_load_serv = []
    for i in range(len(lst)):
        max_load_serv.append(sum(lst[i]))
    print(max_load_serv.index(max(max_load_serv))+1)
    print(max(max_load_serv))
a = []
b = []
for i in range(n):
    for j in range(m):
        b.append(randint(0,20))
    a.append(list(b))
    b.clear()
for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()
print()
MaxLoad(a)
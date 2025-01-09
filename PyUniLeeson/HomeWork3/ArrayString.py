from random import randint
m = int(input('Enter number of columns: '))
n = int(input('Enter number of strings: '))
a = [0]*m
b = [a]*n
for i in range(len(b)):
    for j in range(len(a)):
        a[j]=randint(10,20)
    b.append(a)
    print(b[i][j], end=' ')
    print()
print(max(b[3]))
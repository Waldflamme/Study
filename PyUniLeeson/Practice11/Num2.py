from random import randint
m = int(input('Enter number of columns: '))
n = int(input('Enter number of strings: '))`
chc = input('Enter "main" or "side": ')
def DiagSum(a,chc):
    if chc=='main':
        res = 0
        for i in range(len(a)):
            res += a[i][i]
            if i==len(b)-1:
                break
        print(res)
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
print()
DiagSum(a,chc)
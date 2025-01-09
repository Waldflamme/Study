from random import randint
def column(lst):
    col = []
    for j in range(len(lst[i])):
        col.append(lst[j][i])
    return col
a = []
b = []
for i in range(5):
    for j in range(5):
        b.append(randint(1,30))
    a.append(list(b))
    b.clear()
for i in range(5):
    for j in range(5):
        print(a[i][j], end = ' ')
    print()
print()
l = []
for i in range(5):
    l.append(column(a))
for i in range(5):
    for j in range(4,-1,-1):
        print(l[i][j], end = ' ')
    print()
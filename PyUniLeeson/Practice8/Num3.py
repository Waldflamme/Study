from random import randint
def av_sum(lst1):
    av_sum_tot = []
    for i in range(len(lst1)):
        av_sum_tot.append(sum(lst1[i])/len(lst1[i]))
    avsumtot = sum(av_sum_tot)
    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            if lst1[i][j]>avsumtot:
                lst1[i][j]=lst1[i][j]**2
    return lst1
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
print()
c = av_sum(a)
for i in range(n):
    for j in range(m):
        print(c[i][j], end = ' ')
    print()
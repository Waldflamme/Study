n = int(input('Enter side size: '))
a = [0]*n
b = [a]*n
for i in range(len(b)):
    for j in range(len(a)):
        if j==(n-1)-i:
            a[j] = 1
        else:
            a[j] = 0
        print(b[i][j], end = ' ')
    print()
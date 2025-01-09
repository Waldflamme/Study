n = int(input('Enter side size: '))
a = [0]*n
b = [a]*n
for i in range(len(a)):
    for j in range(len(b)):
        if i==j:
            a[i] = 1
        else:
            a[i] = 0
        print(b[i][j], end = ' ')
    print()
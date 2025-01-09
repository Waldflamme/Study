n = int(input('Enter side size: '))
a = [0]*n
b = [a]*n
count = 0
for i in range(len(b)):
    for j in range(len(a)):
        count += 1
        if count%2 == 0:
            a[j] = 'b'
        else:
            a[j] = 'w'
        print(b[i][j], end = ' ')
    print()
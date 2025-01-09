k = int(input('Enter K: '))

file = open('kDel.txt')
fr = file.readlines()
file.close()

file = open('kDel.txt', 'w')

for s in fr:
    if len(s) < k:
        file.write('')
    else:
        file.write(s[k:])

file.close()
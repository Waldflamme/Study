k = int(input('Enter K: '))

file = open('kstring.txt')
fr = file.readlines()
file.close()

file = open('kstring.txt', 'w')

for s in fr:
    if len(s) < k:
        file.write('')
    else:
        file.write(s[k:])

file.close()
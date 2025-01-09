s = input('Enter s: ')

file = open('sstring.txt')
fr = file.readlines()
file.close()

file = open('sstring.txt', 'w')

for k in fr:
    if k=='\n':
        file.write(f'{s}\n')
    else:
        file.write(k)

file.close()
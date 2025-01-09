k = int(input('Enter K: '))

file = open('num2text.txt')
fr = file.readlines()
file.close()

fr2 = []
for s in fr[0:k]:
    fr2.append(s)
fr2.append('\n')
for s in fr[k:len(fr)]:
    fr2.append(s)

file = open('num2text.txt', 'w+')

for s in fr2:
    file.write(s)

file.close()
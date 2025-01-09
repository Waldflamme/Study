file = open('numstring.txt')
fr = file.readlines()
file.close()

file = open('numstring.txt', 'w+')

for s in fr[1:len(fr)-1]:
        file.write(s)

file.close()
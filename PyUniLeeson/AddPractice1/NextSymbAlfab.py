ln1 = str(input('Enter the line: '))
alf = 'abcdefghijklmopqrstuvwxyz'
for i in range(len(alf)):
    if ln1[0]==alf[i]:
        i+=1
        print('The symbols is', alf[i])
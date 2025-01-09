file = open('num1text.txt')
fr = file.readlines()
file.close()

print(fr)

k = 0
for s in fr:
    if '    ' in s:
        k+=1

print(k)
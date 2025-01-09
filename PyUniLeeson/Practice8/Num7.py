ln = input('Enter a line: ')
st1 = set(())
c = 0
for i in  range(len(ln)):
    if ln[i] not in st1 and ln[i] in '0123456789+-*':
        st1.add(ln[i])
    elif ln[i] in '0123456789+-*':
        c+=1
print(st1)
print(len(st1)+c)
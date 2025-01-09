ln1 = input('Enter a line: ')
ln2 = input('Enter a line: ')
ln3 = input('Enter a line: ')
st1 = set(ln1)
st2 = set(ln2)
st3 = set(ln3)
if st1|st2==st3:
    print('It is possible')
else:
    print('It is impossible')
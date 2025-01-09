lst = [5,1,9,3,8,2,4,6]
lsts = sorted(lst)
st1 = set(lst[0:4:])
st2 = set(lsts[0:4:])
if st1 == st2:
    print('It is sorted')
else:
    print('it is not sorted')
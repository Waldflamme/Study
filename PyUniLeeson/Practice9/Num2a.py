lst = [(1,43,9),(5,96,74),(98,74,63)]
print(type(lst[1]))
st = set()
for i in range(len(lst)):
    for j in range(len(lst[i])):
        st.add(lst[i][j])
tpl = tuple(st)
print(tpl)
print(type(tpl))
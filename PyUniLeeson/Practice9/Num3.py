ln1 = input('Enter a line: ')
ln2 = input('Enter a line: ')
ln3 = input('Enter a line: ')
alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
st1 = set(ln1)
st2 = set(ln2)
st3 = set(ln3)
sm_st = set()
for i in range(len(alf)):
    if alf[i] in st1 and alf[i] in st2 and alf[i] in st3:
        sm_st.add(alf[i])
print(sm_st)
tpl1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
tpl2 = []
for i in range(len(tpl1)):
    if tpl1[i]%2==0:
        tpl2.append(tpl1[i])
print(tuple(tpl2))
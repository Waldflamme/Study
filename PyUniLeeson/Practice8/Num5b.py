lst1 = [(1,2),(),(3,4),(5,6),(),(5,9)]
lst2 = []
for i in range(len(lst1)):
    if len(lst1[i])!=0:
        lst2.append(lst1[i])
print(lst2)
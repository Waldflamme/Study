dic = {'one':'one','two':'two','three':'three','four':'four','five':'five'}
lst = []
for keys in dic:
    if dic[keys][0]!='f':
        lst.append(keys)
for i in range(len(lst)):
    del dic[lst[i]]
print(dic)
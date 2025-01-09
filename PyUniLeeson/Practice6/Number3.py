#3
lst = ['Bang','rule','self','Tree']
alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_case = []
upp_case = []
for i in range(len(lst)):
    if lst[i][0] not in alf:
        low_case.append(lst[i])
for j in range(len(lst)):
    if lst[j][0] in alf:
        upp_case.append(lst[j])
low = sorted(low_case,reverse=True)
upp = sorted(upp_case,reverse=True)
print(lst)
print(low+upp)

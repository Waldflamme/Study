arr = [[1,1,1],[1,1,1],[1,99,1]]
for i in range(3):
    for j in range(3):
        print(arr[i][j], end=' ')
    print()
def av_sum(lst1):
    av_sum_tot = []
    for i in range(len(lst1)):
        av_sum_tot.append(sum(lst1[i])/len(lst1[i]))
    avsumtot = sum(av_sum_tot)
    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            if lst1[i][j]>avsumtot:
                lst1[i][j]=lst1[i][j]**2
    return lst1
arr_av_s = av_sum(arr)

for i in range(3):
    for j in range(3):
        print(arr_av_s[i][j], end=' ')
    print()
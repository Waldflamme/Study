ls = [11,5,11,7,8,11,5,7]

def CountOccurrences(lst):
    dc_ls = []
    pair = []
    for i in lst:
        count = 0
        for j in lst:
            if j==i:
                count +=1
        pair.append(i)
        pair.append(count)
        dc_ls.append(tuple(pair))
        count = 0
        pair.clear()
    d = {}
    d.update(dc_ls)
    print(d)

print(ls)
CountOccurrences(ls)
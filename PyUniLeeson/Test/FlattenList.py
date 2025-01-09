ls = [[1,2,3],['a','b','c'],[5,8,4]]

def FlattenList(lst):
    lt = []
    for i in lst:
        for j in i:
            lt.append(j)
    return lt
print(FlattenList(ls))
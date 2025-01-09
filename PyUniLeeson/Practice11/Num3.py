ls_tp = [(1,9,'p'),(78,49,'hp',28),('y',45,89)]
def ReverseTuples(lst):
    ls = []
    tp = []
    for i in ls_tp:
        for j in i[::-1]:
            tp.append(j)
        ls.append(tuple(tp))
        tp.clear()
    return ls
print(ReverseTuples(ls_tp))
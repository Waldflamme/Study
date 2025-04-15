ls = [1, 2, 3, 4]

def new_array(ls):
    N = len(ls)
    new_ls = [0] * N
    res = 0

    for i in reversed(range(N)):
        res += ls[i]
        new_ls[i] = res

    return new_ls

print(new_array(ls))
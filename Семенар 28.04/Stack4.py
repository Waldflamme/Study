st = [12, 5, 3, 8, -12, -10, 1, 9, 2, 0]

def no_neg(st):

    no_neg_st = []
    while st:
        val = st.pop()
        if val>=0:
            no_neg_st.append(val)

    res_st = []
    while no_neg_st:
        res_st.append(no_neg_st.pop())

    return res_st

print(st)
print()
print(no_neg(st))
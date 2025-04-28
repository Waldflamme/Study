st = [1, 2, 3, 4, 5]

def rev_st(st):
    rev_st = []
    while st:
        rev_st.append(st.pop())
    return rev_st

print(st)
print()
print(rev_st(st))

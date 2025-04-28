st = [1, 17, 10, 2, 3, 4, 5, 6, 7, 8, 9]

def simple(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def filter_st(st):
    temp_st = []

    while st:
        val = st.pop()
        if simple(val):
            temp_st.append(val)
            
    result_st = []
    while temp_st:
        result_st.append(temp_st.pop())

    return result_st

print(st)
print()
print(filter_st(st))
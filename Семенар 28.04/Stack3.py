st = [12, 5, 3, 8, 1, 9, 2, 0]

def find_extreme(st, find_max_min=True):
    if not st:
        return None

    extreme = st.pop()

    while st:
        val = st.pop()
        if find_max_min:
            if val > extreme:
                extreme = val
        else:
            if val < extreme:
                extreme = val

    return extreme

print(find_extreme(st.copy(), find_max_min=True))
print()
print(find_extreme(st.copy(), find_max_min=False))
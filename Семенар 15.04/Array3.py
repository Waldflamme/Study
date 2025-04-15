ls = [3, 7, 2, 8, 4]
r = 10

def close_pair_sum(ls, r):
    if len(ls) < 2:
        return None

    min_diff = 0
    best_pair = (ls[0], ls[1])

    for i in range(len(ls) - 1):
        a, b = ls[i], ls[i + 1]
        s = a + b
        diff = abs(r - s)

        if diff < min_diff:
            min_diff = diff
            best_pair = (a, b)

    return best_pair

print(close_pair_sum(ls, r))
R = 10
ls = [3, 7, 2, 8, 4]

def closest_sum_to_r(ls, R):
    if len(ls) < 2:
        return None

    min_diff = 0
    result = (ls[0], ls[1])

    for i in range(len(ls) - 1):
        a, b = ls[i], ls[i + 1]
        pair_sum = a + b
        diff = abs(R - pair_sum)

        if diff < min_diff:
            min_diff = diff
            result = (a, b)

    return result

a, b = closest_sum_to_r(ls, R)
print(a, b)
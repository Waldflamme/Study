ls = [1, 1, 2, 3, 3, 3, 4, 4]
l = 3

def replace_short_series(ls, l):
    if not ls:
        return []

    result = []
    i = 0
    N = len(ls)

    while i < N:
        current = ls[i]
        count = 1

        while i + count < N and ls[i + count] == current:
            count += 1

        if count < l:
            result.append(0)
        else:
            result.extend([current] * count)

        i += count

    return result

print(replace_short_series(ls, l))
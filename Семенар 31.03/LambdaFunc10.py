ls1 = [1, 2, 3, 4, 5, 6, 7, 8]
ls2 = [2, 2, 3, 1, 2, 6, 7, 9]

pairs_equal = list(map(lambda x, y: x == y, ls1, ls2))

count_equal_pairs = pairs_equal.count(True)

print(count_equal_pairs)

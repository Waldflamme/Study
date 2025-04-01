ls1 = [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]
ls2 = [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]

def ratio_of_numbers(ls):
    n = len(ls)

    positive = len(list(filter(lambda x: x > 0, ls)))
    negative = len(list(filter(lambda x: x < 0, ls)))
    zeros = len(list(filter(lambda x: x == 0, ls)))

    return round(positive / n, 2), round(negative / n, 2), round(zeros / n, 2)

print(ratio_of_numbers(ls1))
print(ratio_of_numbers(ls2))

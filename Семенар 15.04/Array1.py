x = [1, 3, 2]
y = [4, 1, 3]

def sort_point(x, y):
    points = list(zip(x, y))

    points.sort(key=lambda p: (p[0] + p[1], p[0]), reverse=True)

    x_sorted, y_sorted = zip(*points)
    return list(x_sorted), list(y_sorted)

x_sorted, y_sorted = sort_point(x, y)
print(x_sorted)
print(y_sorted) 
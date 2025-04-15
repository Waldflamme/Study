x = [-3, 1, -5, -2]
y = [4, 5, -1, 6]

def most_distant(x, y):
    max_dist_sq = 0
    result = (0, 0)

    for x, y in zip(x, y):
        if x < 0 and y > 0:
            dist_sq = x**2 + y**2
            if dist_sq > max_dist_sq:
                max_dist_sq = dist_sq
                result = (x, y)

    return result

print(most_distant(x, y))
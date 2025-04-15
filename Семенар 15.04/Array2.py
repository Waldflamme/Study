ls = [1, 4, 7, 10]
r = 6

def nearest_element(ls, r):
    return min(ls, key=lambda x: abs(x - r))

print(nearest_element(ls, r))
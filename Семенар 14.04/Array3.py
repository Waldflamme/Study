from collections import Counter

ls = [1, 2, 2, 3, 4, 4, 4, 5]

def same_two(ls):
    freq = Counter(ls)
    result = [x for x in ls if freq[x] != 2]
    return result

new_ls = same_two(ls)
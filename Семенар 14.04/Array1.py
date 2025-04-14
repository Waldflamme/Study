def increasing_spaces(arr):
    if not arr:
        return 0

    count = 0
    i = 0
    n = len(arr)

    while i < n-1:
        if arr[i] < arr[i+1]:
            while i < n-1 and arr[i] < arr[i+1]:
                i += 1
            count += 1
        else:
            i += 1

    return count

print(increasing_spaces([1, 2, 1, 3, 4, 0, 2]))
print(increasing_spaces([5, 4, 3, 2]))
print(increasing_spaces([1, 2, 3, 4]))
print(increasing_spaces([]))
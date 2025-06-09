import time
import random
from copy import deepcopy

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения функции {func.__name__}: {end - start:.6f} сек.\n")
        return result
    return wrapper

songs = [
    ("Artist A", "Song A", 2020, 4.5),
    ("Artist B", "Song B", 2018, 4.7),
    ("Artist C", "Song C", 2021, 4.0),
    ("Artist D", "Song D", 2019, 3.9),
    ("Artist E", "Song E", 2023, 4.8),
    ("Artist F", "Song F", 2017, 4.3),
]

@calculate_time
def selection_sort(data):
    arr = deepcopy(data)
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j][2] > arr[max_idx][2]:  # по году
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

@calculate_time
def insertion_sort(data):
    arr = deepcopy(data)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[2] > arr[j][2]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

@calculate_time
def quick_sort(data):
    arr = deepcopy(data)

    def _quick_sort(items):
        if len(items) <= 1:
            return items
        pivot = items[0]
        left = [x for x in items[1:] if x[2] > pivot[2]]
        right = [x for x in items[1:] if x[2] <= pivot[2]]
        return _quick_sort(left) + [pivot] + _quick_sort(right)

    return _quick_sort(arr)

@calculate_time
def merge_sort(data):
    arr = deepcopy(data)

    def _merge_sort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = _merge_sort(lst[:mid])
        right = _merge_sort(lst[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        while left and right:
            if left[0][2] >= right[0][2]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left + right)
        return result

    return _merge_sort(arr)

if __name__ == "__main__":
    print("Сортировка выбором:")
    sorted_selection = selection_sort(songs)
    for song in sorted_selection:
        print(song)

    print("\nСортировка вставками:")
    sorted_insertion = insertion_sort(songs)
    for song in sorted_insertion:
        print(song)

    print("\nБыстрая сортировка:")
    sorted_quick = quick_sort(songs)
    for song in sorted_quick:
        print(song)

    print("\nСортировка слиянием:")
    sorted_merge = merge_sort(songs)
    for song in sorted_merge:
        print(song)
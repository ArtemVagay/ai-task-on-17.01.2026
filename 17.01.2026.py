import collections
import random
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def a(array):
#     direct = int(input())
#     return array[-direct:] + array[:-direct]
# print(a(array))
#
# # 1
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# new_matrix = []
# def left_shift(mtr):
#     for rw in mtr:
#         new_matrix.append(rw[1:] + rw[:1])
#
# left_shift(matrix)
# for row in new_matrix:
#     for el in row:
#         print(el, end=" ")
#     print()
#
# # 2
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# new_matrix = []
# def left_shift(mtr):
#     for rw in mtr:
#         new_matrix.append(rw[-1:] + rw[:-1])
#
# left_shift(matrix)
# for row in new_matrix:
#     for el in row:
#         print(el, end=" ")
#     print()
# # 3
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# new_matrix = []
# def left_shift(mtr):
#     direct = int(input())
#     for rw in mtr:
#         new_matrix.append(rw[direct:] + rw[:direct])
#
# left_shift(matrix)
# for row in new_matrix:
#     for el in row:
#         print(el, end=" ")
#     print()
from itertools import count

# # 1
# matrix = [[1, 2, 3, 1],
#           [4, 5, 6, 3],
#           [7, 8, 9, 5]]
#
# def up_side_down_shift(mtr):
#     return mtr[::-1]
#
# matrix = up_side_down_shift(matrix)
# for row in matrix:
#     for el in row:
#         print(el, end=" ")
#     print()
#
# # 2
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# new_matrix = [[] for _ in range(len(matrix))]
# def transpose_matrix(mtr):
#     for y in range(len(mtr)):
#         for x in range(len(mtr[y])):
#             new_matrix[y].append(mtr[x][y])
#
# matrix = transpose_matrix(matrix)
# for row in new_matrix:
#     for el in row:
#         print(el, end=" ")
#     print()
#
# # 3
# matrix = [[1, 2, 3, 4],
#           [4, 5, 6, 5],
#           [7, 8, 9, 10]]
#
#
# def transpose_matrix(mtr):
#     rows = len(mtr)
#     cols = len(mtr[0])
#     res = [[] for _ in range(cols)]
#
#     for y in range(rows):
#         for x in range(cols):
#             res[x].append(mtr[y][x])
#     return res
#
#
# new_matrix = transpose_matrix(matrix)
#
# for row in new_matrix:
#     for el in row:
#         print(el, end=" ")
#     print()

# # 1 и 2
# matrix = [[1, 2, 2], [5, 5, 6], [7, 9, 9]]
#
# lst = [el for row in matrix for el in row]
# counts = collections.Counter(lst)
# print(counts)
#
# print("Ответ на первую")
# for num, count in counts.items():
#     if count > 1:
#         print(num, count)
#
# print("Ответ на вторую")
# for num, count in counts.items():
#     if count == 1:
#         print(num)
#
# # 3
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# multy = 1
# for y in range(len(matrix)):
#     for x in range(len(matrix[y])):
#         if x == y:
#             multy *= matrix[y][x]
# print(multy)

# end


import random, time


def generate_alternating_step_list(n, start_val, step):
    result = []
    current_val = start_val
    for i in range(n):
        if i % 2 == 0:
            result.append(round(current_val, 7))
        else:
            result.append(round(-current_val, 7))
        current_val += step

    return result
small_lst = generate_alternating_step_list(100, 0.000052, 0.000001)
print(small_lst)

huge_lst = [random.randint(-100_000, 100_000) for _ in range(100)]
print(huge_lst)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def quick_sort(array):
    if len(array) <= 1:
        return array
        # базовый случай когда массив состоит из 0 или 1 элемента

    pivot = array[random.randint(0, len(array) - 1)]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

def bucket_sort(arr):
    if not arr:
        return arr

    n = len(arr)
    min_val = min(arr)
    max_val = max(arr)

    if min_val == max_val:
        return arr

    buckets = [[] for _ in range(n)]

    data_range = max_val - min_val

    for value in arr:
        index = int((value - min_val) / data_range * (n - 1))
        buckets[index].append(value)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

time1_bubbles = time.time()
bubble_sort(small_lst)
print(f"Маленький список у пузырьков скорость {int((time.time() - time1_bubbles) * 1_000_000_000)} наносек")
time2_bubbles = time.time()
bubble_sort(huge_lst)
print(f"Большой список у пузырьков скорость {int((time.time() - time2_bubbles) * 1_000_000_000)} наносек")

time1_quick = time.time()
quick_sort(small_lst)
print(f"Маленький список у быстрой скорость {int((time.time() - time1_quick) * 1_000_000_000)} наносек")
time2_quick = time.time()
quick_sort(huge_lst)
print(f"Большой список у быстрой скорость {int((time.time() - time2_quick) * 1_000_000_000)} наносек")

time1_merge = time.time()
merge_sort(small_lst)
print(f"Маленький список у слияния скорость {int((time.time() - time1_merge) * 1_000_000_000)} наносек")
time2_merge = time.time()
merge_sort(huge_lst)
print(f"Большой список у слияния скорость {int((time.time() - time2_merge) * 1_000_000_000)} наносек")

time1_bucket = time.time()
bucket_sort(small_lst)
print(f"Маленький список у блочной скорость {int((time.time() - time1_bucket) * 1_000_000_000)} наносек")
time2_bucket = time.time()
bucket_sort(huge_lst)
print(f"Большой список у блочной скорость {int((time.time() - time2_bucket) * 1_000_000_000)} наносек")
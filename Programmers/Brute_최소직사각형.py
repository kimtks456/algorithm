def solution(numbers):
    x, y = 0, 0
    for i in range(len(numbers)):
        if numbers[i][0] < numbers[i][1]:
            numbers[i][1], numbers[i][0] = numbers[i][0], numbers[i][1]
        if x < numbers[i][0]:
            x = numbers[i][0]
        if y < numbers[i][1]:
            y = numbers[i][1]
    return x * y

# 뇌를 비운 풀이
# from itertools import combinations as cb
# from copy import deepcopy
#
#
# def get_size(sizes):
#     maxx, maxy = 0, 0
#     for x, y in sizes:
#         if maxx < x:
#             maxx = x
#         if maxy < y:
#             maxy = y
#     return maxx * maxy
#
#
# def flip(sizes, idx):
#     min_size = 1000000
#     for item in idx:
#         temp_sizes = deepcopy(sizes)
#         for i in range(len(item)):
#             j = item[i]
#             temp_sizes[j][0], temp_sizes[j][1] = temp_sizes[j][1], temp_sizes[j][0]
#         temp_size = get_size(temp_sizes)
#         if min_size > temp_size:
#             min_size = temp_size
#     return min_size
#
#
# def solution(sizes):
#     answer = 1000000
#     comb = []
#     idx = [i for i in range(len(sizes))]
#     for i in range(1, len(sizes)):
#         comb.append(list(cb(idx, i)))
#
#     for item in comb:
#         now_size = flip(sizes, item)
#         if now_size < answer:
#             answer = now_size
#     return answer

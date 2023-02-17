# from itertools import combinations
#
# def solution(nums):
#     answer = 0
#
#     for target in list(combinations(nums, len(nums) // 2)):
#         print(target)
#         temp = len(set(target))
#         if temp > answer:
#             answer = temp
#
#     return answer

def solution(nums):
    maximum = len(set(nums))

    if len(nums) // 2 < maximum:
        return len(nums) // 2
    else:
        return maximum
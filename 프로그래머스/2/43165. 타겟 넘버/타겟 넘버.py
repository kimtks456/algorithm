def solution(numbers, target):
    return dfs(numbers, 0, target)

def dfs(numbers, i, target):
    if i == len(numbers):
        return sum(numbers) == target
    numbers1 = numbers[:i] + [numbers[i]] + numbers[i+1:]
    numbers2 = numbers[:i] + [-numbers[i]] + numbers[i+1:]
    return sum([dfs(numbers1, i+1, target), dfs(numbers2, i+1, target)])



# def dfs(numbers, idx, target):
#     if idx == len(numbers):
#         if sum(numbers) == target:
#             return 1
#         return 0
#     
#     numbers2 = numbers[:]
#     numbers2[idx] = -numbers[idx]
#     return dfs(numbers, idx+1, target) + dfs(numbers2, idx+1, target)
# 
# def solution(numbers, target):
#     answer = 0
#     answer = dfs(numbers, 0, target)
#     return answer
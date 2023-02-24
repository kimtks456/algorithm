def dfs(numbers, idx, target):
    if idx == len(numbers):
        if sum(numbers) == target:
            return 1
        return 0

    numbers2 = numbers[:]
    numbers2[idx] = -numbers[idx]
    return dfs(numbers, idx + 1, target) + dfs(numbers2, idx + 1, target)


def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, 0, target)
    return answer
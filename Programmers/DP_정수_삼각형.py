from copy import deepcopy


def solution(triangle):
    answer = 0
    depth = len(triangle)
    value = deepcopy(triangle)

    for i in range(1, depth):
        value[i][0] = value[i - 1][0] + triangle[i][0]
        value[i][-1] = value[i - 1][-1] + triangle[i][-1]

        for j in range(1, i):
            value[i][j] = max(value[i - 1][j - 1] + triangle[i][j], value[i - 1][j] + triangle[i][j])

    answer = max(value[-1])
    return answer
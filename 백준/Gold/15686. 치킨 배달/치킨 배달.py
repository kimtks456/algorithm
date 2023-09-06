import sys
import copy


n, m = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

home, chicken = [], []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            home.append((i, j))
        if maps[i][j] == 2:
            chicken.append((i, j))


def combination(arr, r):
    result = []

    def dfs(chosen, depth):
        if len(chosen) == r:
            result.append(copy.deepcopy(chosen))
            return
        if depth == len(arr):
            return

        chosen.append(arr[depth])
        dfs(chosen, depth + 1)

        chosen.pop()
        dfs(chosen, depth + 1)

    dfs([], 0)
    return result

cases = combination(chicken, m)
chicken_distance = 10000000
for case in cases:
    temp_chicken_distance = 0
    for i, j in home:
        distances = [abs(i-case[k][0]) + abs(j-case[k][1]) for k in range(len(case))]
        temp_chicken_distance += min(distances)

    if temp_chicken_distance < chicken_distance:
        chicken_distance = temp_chicken_distance

print(chicken_distance)



'''

5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
= 6 + 4
'''
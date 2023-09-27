import sys
from copy import deepcopy


def combination(arr, r):
    case = []

    def bfs(temp, depth):
        if len(temp) == r:
            case.append(temp[:])
            return
        if depth == len(arr):
            return

        temp.append(arr[depth])
        bfs(temp, depth + 1)

        temp.pop()
        bfs(temp, depth + 1)

    bfs([], 0)

    return case


def solve(archer_y_position, maps):
    kill = 0
    archer_x = len(maps)

    while archer_x > 0:
        for y in archer_y_position:
            print(archer_x, y)
            temp_d = 1
            while temp_d <= d:
                print(temp_d)
                for j in range(y - temp_d + 1, y + temp_d):
                    i = archer_x - temp_d - abs(j - y)
                    print(i, j)
                temp_d += 1
            print()
        archer_x -= 1
    return 1
# abs(j - y) + abs(i - castle_row) = temp_d


n, m, d = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cases = combination([i for i in range(m)], 3)
answer = 0

for case in cases:
    print("Now : ", case)
    temp = solve(case, deepcopy(maps))
    answer = max(answer, temp)

print(answer)

"""
5 5 3
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0

"""
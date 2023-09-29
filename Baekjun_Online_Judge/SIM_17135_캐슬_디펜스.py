import sys
from copy import deepcopy


def combination(arr, r):
    result = []

    def bfs(temp, depth):
        if len(temp) == r:
            result.append(temp[:])
            return
        if depth == len(arr):
            return

        temp.append(arr[depth])
        bfs(temp, depth + 1)

        temp.pop()
        bfs(temp, depth + 1)

    bfs([], 0)

    return result


def solve(archer_y_position, maps):
    kill = 0
    archer_x = len(maps)

    # 한칸씩 궁수들을 전진시킴
    while archer_x > 0:
        # print("now row : ", archer_x)
        # for row in maps:
        #     print(row)
        # print()
        for y in archer_y_position:
            temp_d = 1
            # 최소 거리에서 적 발견하면, flag를 통해 다음 최소거리는 탐색 안함.
            flag = True

            # 최소 거리 먼저 탐색
            while temp_d <= d and flag:

                # 왼쪽부터 탐색
                for j in range(y - temp_d + 1, y + temp_d):
                    i = archer_x - temp_d + abs(j - y)
                    if i < 0 or 0 > j or j > len(maps[0]) - 1:
                        continue
                    if maps[i][j] == 1:
                        maps[i][j] = 2
                        kill += 1
                        flag = False
                        break

                    # 이전 궁수가 맞춘 적이라면, 한번 더 맞추고 다음 궁수 탐색
                    if maps[i][j] == 2:
                        flag = False
                        break
                else:
                    temp_d += 1
        # 모든 궁수를 탐색했다면, 사살한 적을 다시 0으로 바꿈
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == 2:
                    maps[i][j] = 0
        archer_x -= 1
    return kill
# abs(j - y) + abs(i - castle_row) = temp_d


n, m, d = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cases = combination([i for i in range(m)], 3)
answer = 0

for case in cases:
    # print("Now : ", case)
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
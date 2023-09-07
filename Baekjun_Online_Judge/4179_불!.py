import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
fire = []

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'J':
            start = (i, j)
        if maps[i][j] == 'F':
            fire.append((i, j))

mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0
que = deque([(start[0], start[1], 0)])
maps_per_time = [maps]
next_fire = []
flag = False

while que:
    x, y, time = que.popleft()

    if x == n - 1 or y == m - 1:
        print(time + 1)
        flag = True
        break

    # 불 번지기
    if len(maps_per_time) == time:
        while fire:
            fx, fy = fire.pop()
            for dx, dy in mv:
                nx, ny = fx + dx, fy + dy

                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] in ('.', 'J'):
                    maps[nx][ny] = 'F'
                    next_fire.append((nx, ny))

        maps_per_time.append(maps)
        fire = next_fire
        next_fire = []
        maps = maps_per_time[time]
    else:
        maps = maps_per_time[time]

    # # 불 번진곳과 지훈 이동한 곳이 같다면, continue
    # if maps[x][y] == 'F':
    #     continue


    # 지훈 이동
    for dx, dy in mv:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == '.':
            que.append((nx, ny, time + 1))

    # print("after : ", x, y, time)
    # for temp in maps_per_time:
    #     for row in temp:
    #         print(row)
    #     print()
    # print('##############')

if not flag:
    print("IMPOSSIBLE")

'''

4 4
####
#JF#
#.F#
#..#


4 5
#####
#J...
#F..#
#...#

'''
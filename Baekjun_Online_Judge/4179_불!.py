import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
fire = []

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'J':
            start = (i, j, 0)
        if maps[i][j] == 'F':
            fire.append((i, j, 0))

mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]

que_f = deque(fire)
que_j = deque([start])

visited_f = [[1 if (j, i) in fire else 0 for i in range(m)] for j in range(n)]
visited_j = [[0 for j in range(m)] for j in range(n)]
visited_j[start[0]][start[1]] = 1

while que_f:
    x, y, time = que_f.popleft()
    for dx, dy in mv:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] in ('.', 'J') and visited_f[nx][ny] == 0:
            visited_f[nx][ny] = time + 1
            que_f.append((nx, ny, time + 1))

# for row in visited_f:
#     print(row)

while que_j:
    x, y, time = que_j.popleft()
    # print(x,y,time, visited_j)
    if x in (0, n - 1) or y in (0, m - 1):
        print(time + 1)
        break
    for dx, dy in mv:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == '.':
            if (not visited_f[nx][ny] or visited_f[nx][ny] > time + 1) and visited_j[nx][ny] == 0:
                visited_j[nx][ny] = time + 1
                que_j.append((nx, ny, time + 1))
else:
    print("IMPOSSIBLE")



# 메모리 초과난 풀이
# import sys
# from collections import deque
#
#
# n, m = map(int, sys.stdin.readline().split())
# maps = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
# fire = []
#
# for i in range(n):
#     for j in range(m):
#         if maps[i][j] == 'J':
#             start = (i, j)
#         if maps[i][j] == 'F':
#             fire.append((i, j))
#
# mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# answer = 0
# que = deque([(start[0], start[1], 0)])
# maps_per_time = [maps]
# next_fire = []
# flag = False
#
# while que:
#     x, y, time = que.popleft()
#
#     if x == n - 1 or y == m - 1:
#         print(time + 1)
#         flag = True
#         break
#
#     # 불 번지기
#     if len(maps_per_time) == time:
#         while fire:
#             fx, fy = fire.pop()
#             for dx, dy in mv:
#                 nx, ny = fx + dx, fy + dy
#
#                 if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] in ('.', 'J'):
#                     maps[nx][ny] = 'F'
#                     next_fire.append((nx, ny))
#
#         maps_per_time.append(maps)
#         fire = next_fire
#         next_fire = []
#         maps = maps_per_time[time]
#     else:
#         maps = maps_per_time[time]
#
#     # # 불 번진곳과 지훈 이동한 곳이 같다면, continue
#     # if maps[x][y] == 'F':
#     #     continue
#
#
#     # 지훈 이동
#     for dx, dy in mv:
#         nx, ny = x + dx, y + dy
#
#         if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == '.':
#             que.append((nx, ny, time + 1))
#
#     # print("after : ", x, y, time)
#     # for temp in maps_per_time:
#     #     for row in temp:
#     #         print(row)
#     #     print()
#     # print('##############')
#
# if not flag:
#     print("IMPOSSIBLE")

'''
2 2
..
JF

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
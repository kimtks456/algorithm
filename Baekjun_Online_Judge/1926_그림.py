import sys
from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
def bfs(start):
    mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    que = deque()
    que.append(start)
    area = 1

    while que:
        x, y = que.popleft()

        for dx, dy in mv:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and maps[nx][ny] == 1 and (nx, ny):
                maps[nx][ny] = 0
                que.append((nx, ny))
                area += 1
    return area


count, area = 0, 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            maps[i][j] = 0
            temp_area = bfs((i, j))
            if temp_area > area:
                area = temp_area
            count += 1

# visited를 쓰니 시간초과남
# def bfs(start, visited):
#     mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     que = deque()
#     que.append(start)
#     area = 1
#
#     while que:
#         x, y = que.popleft()
#
#         for dx, dy in mv:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and maps[nx][ny] == 1 and (nx, ny) not in visited:
#                 visited.append((nx, ny))
#                 que.append((nx, ny))
#                 area += 1
#     return area
#
#
# count, area = 0, 0
# visited = []
#
# for i in range(n):
#     for j in range(m):
#         if maps[i][j] == 1 and (i, j) not in visited:
#             visited.append((i, j))
#             print(i,j)
#             temp_area = bfs((i, j), visited)
#             print(visited)
#             if temp_area > area:
#                 area = temp_area
#             count += 1

print(count)
print(area)

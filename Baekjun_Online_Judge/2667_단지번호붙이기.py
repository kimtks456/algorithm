import sys
from collections import deque


def bfs(start, num_of_sector):
    visited = set()
    visited.add(start)
    que = deque()
    que.append(start)

    while que:
        x, y = que.popleft()

        for dx, dy in mv:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= n-1 and 0 <= ny <= n-1 and (nx, ny) not in visited and maps[nx][ny] == 1:
                visited.add((nx, ny))
                que.append((nx, ny))
                maps[nx][ny] = num_of_sector


n = int(input())
maps = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
sector = 2

mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            maps[i][j] = sector
            bfs((i, j), sector)
            sector += 1

# 단지내 집 수 계산
answer = []
sector -= 1
for i in range(2, sector + 1):
    count = 0
    for x in range(n):
        for y in range(n):
            if maps[x][y] == i:
                count += 1
    answer.append(count)

print(sector - 1)
for i in sorted(answer):
    print(i)

'''
5
10101
01010
00000
00000
00000
'''
from collections import deque
import sys
input = sys.stdin.readline


def dfs(sx, sy):
    que = deque([(sx, sy)])
    maps[sy][sx] = 0
    area = 1

    while que:
        x, y = que.popleft()

        for dx, dy in mv:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                que.append((nx, ny))
                area += 1

    return area


N, M, K = map(int, input().split())
maps = [[1 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            maps[i][j] = 0

visited = [[False for _ in range(M)] for _ in range(N)]
answer = 0
mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = []


for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            temp = dfs(j, i)
            result.append(temp)

result.sort()

print(len(result))
for v in result:
    print(v)
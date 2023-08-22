from collections import deque
import sys


n, m = map(int, input().split())
maps = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
queue = deque()
visited = []
queue.append((0, 0, 1))
visited.append((0, 0))

move = [(0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)]

while queue:
    x, y, count = queue.popleft()

    if (x, y) == (m - 1, n - 1):
        print(count)
        break

    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1 and (nx, ny) not in visited:
            queue.append((nx, ny, count + 1))
            visited.append((nx, ny))
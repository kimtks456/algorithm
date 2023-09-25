from sys import stdin
from collections import deque


n = int(stdin.readline())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
answer = 0

# bfs : (x, y, direction(가로=0, 세로=1, 대각선=2))
que = deque([(0, 1, 0)])
mv = [[(0, 1), (1, 1)],
      [(1, 0), (1, 1)],
      [(0, 1), (1, 0), (1, 1)]]

while que:
    x, y, direction = que.popleft()

    if x == n - 1 and y == n - 1:
        answer += 1
        continue

    for i, dd in enumerate(mv[direction]):
        nx, ny = x + dd[0], y + dd[1]

        if 0 <= nx < n and 0 <= ny < n:
            # 빈 칸이어야 하는 곳 확인
            if maps[nx][ny] == 1:
                continue

            if i == len(mv[direction]) - 1:
                if maps[nx - 1][ny] or maps[nx][ny - 1]:
                    continue

            # 다음 방향 결정
            next_direction = 0

            if direction == 0:
                next_direction = 0 if i == 0 else 2
            elif direction == 1:
                next_direction = 1 if i == 0 else 2
            else:
                next_direction = i

            que.append((nx, ny, next_direction))

print(answer)

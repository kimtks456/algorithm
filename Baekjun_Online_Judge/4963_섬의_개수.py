import sys


def dfs(x, y, maps):
    dx_list = [0, 1, 1, 1, 0, -1, -1, -1]
    dy_list = [-1, -1, 0, 1, 1, 1, 0, -1]

    stack = [(x, y)]
    visited = set()

    while stack:
        x, y = stack.pop()

        maps[y][x] = 0

        if (x, y) in visited:
            continue

        for dx, dy in zip(dx_list, dy_list):
            nx, ny = x + dx, y + dy
            if 0 <= nx <= w - 1 and 0 <= ny <= h - 1 and maps[ny][nx] == 1 and (nx, ny) not in visited:
                stack.append((nx, ny))

        visited.add((x, y))


while True:
    w, h = map(int, input().split())
    count = 0

    if w == 0 and h == 0:
        break

    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                dfs(j, i, maps)
                count += 1

    print(count)


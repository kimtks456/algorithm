import sys
read = sys.stdin.readline


# input
n, m = map(int, read().split())
sx, sy, d = map(int, read().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, read().split())))

# Initialize
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[sx][sy] = 1
mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 1
stack = [(sx, sy, d)]

# DFS
while stack:
    x, y, d = stack.pop()

    # Check uncleaned room
    flag = True
    for dx, dy in mv:
        nx, ny = x+dx, y+dy
        flag = flag and (visited[nx][ny] == 1 or maps[nx][ny] == 1)
        if flag == False:
            break

    # Rollback to before room
    if flag == True:
        dx, dy = mv[d]
        nx, ny = x + dx*(-1), y + dy*(-1)
        # Check before node is wall
        if maps[nx][ny] == 1:
            break
        stack.append((nx, ny, d))
        # print("Rollback")
        continue

    # Choose next direction
    nd = d - 1 if d-1 >= 0 else 3
    dx, dy = mv[nd]
    nx, ny = x+dx, y+dy
    while visited[nx][ny] == 1 or maps[nx][ny] == 1:
        if maps[nx][ny] == 1:
            nd = nd - 1 if nd - 1 >= 0 else 3
            dx, dy = mv[nd]
            nx, ny = x + dx, y + dy
            continue
        nd = nd - 1 if nd-1 >= 0 else 3
        dx, dy = mv[nd]
        nx, ny = x + dx, y + dy

    # Push to Stack
    if maps[nx][ny] == 0:
        stack.append((nx, ny, nd))
        visited[nx][ny] = 1
        result += 1
        # print(nx, ny, nd)

print(result)

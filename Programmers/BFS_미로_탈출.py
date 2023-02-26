from collections import deque


def bfs(sx, sy, ex, ey, maps):
    q = deque([(sx, sy, 0)])
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[sx][sy] = True

    mv = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        x, y, t = q.popleft()
        if x == ex and y == ey:
            return t

        for dx, dy in mv:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                # if not visited[nx][ny] and (maps[nx][ny] == 'O' or maps[nx][ny] == maps[ex][ey]):
                # S도 지나갈 수 있어야함.
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    q.append((nx, ny, t + 1))

    return -1


def solution(maps):
    answer = 0

    # find S,L,E
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                sx, sy = i, j
            if maps[i][j] == 'L':
                lx, ly = i, j
            if maps[i][j] == 'E':
                ex, ey = i, j

    t1 = bfs(sx, sy, lx, ly, maps)
    t2 = bfs(lx, ly, ex, ey, maps)
    answer = t1 + t2
    if t1 == -1 or t2 == -1:
        answer = -1
    return answer

# maps = ["SOOOL",
#         "XXXXO",
#         "OOOOO",
#         "OXXXX",
#         "OOOOE"]

# maps = ["OOOOOL",
#         "OXOXOO",
#         "OOSXOX",
#         "OXXXOX",
#         "EOOOOX"]
# print(solution(maps))

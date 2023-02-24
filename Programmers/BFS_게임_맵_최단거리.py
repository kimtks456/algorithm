from collections import deque


def solution(maps):
    answer = 1
    q = deque()
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q.append((0, 0, answer))
    visited[0][0] = True
    temp = 1

    while q:
        x, y, temp = q.popleft()

        if x == n - 1 and y == m - 1:
            answer = temp
            break

        for mx, my in move:
            nx, ny = x + mx, y + my
            if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and visited[nx][ny] is False and maps[nx][ny] == 1:
                q.append((nx, ny, temp + 1))
                visited[nx][ny] = True

    if x != n - 1 or y != m - 1:
        answer = -1

    return answer

a = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
b = a[:]
b[0][0] = 1011
print(a)
print(b)
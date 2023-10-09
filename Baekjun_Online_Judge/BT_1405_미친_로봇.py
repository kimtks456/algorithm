def dfs(start, p, count):
    global answer

    if count == n:
        answer += p
        return

    x, y = start[0], start[1]

    for i, d in enumerate(mv):
        nx, ny = x + d[0], y + d[1]
        if not maps[nx][ny] and prob[i]:
            maps[nx][ny] = True
            dfs((nx, ny), p * prob[i], count + 1)
            maps[nx][ny] = False


prob = list(map(int, input().split()))
n = prob[0]
prob = list(map(lambda x: x / 100, prob[1:]))
answer = 0

maps = [[False for _ in range(29)] for _ in range(29)]
maps[14][14] = True
# x, y, 확률, 이동 횟수
stack = [(14, 14, 0, 0)]
# 동, 서, 남, 북
mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]

dfs((14, 14), 1, 0)
print(f'{answer:.9f}')
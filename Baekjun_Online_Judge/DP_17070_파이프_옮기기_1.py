from sys import stdin


n = int(stdin.readline())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
answer = 0

# 가로(0), 세로(1), 대각선(2)
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
for i in range(1, n):
    if maps[0][i] == 1:
        break
    dp[0][i][0] = 1

for i in range(1, n):
    for j in range(2, n):
        if maps[i][j] == 1:
            continue

        dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
        dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
        if maps[i - 1][j] or maps[i][j - 1]:
            continue
        dp[i][j][2] = sum(dp[i - 1][j - 1])

print(sum(dp[n - 1][n - 1]))
# print(dp[n - 1][n - 1])
# print(dp[0])
# print(dp[1])


# # bfs : (x, y, direction(가로=0, 세로=1, 대각선=2))
# que = deque([(0, 1, 0)])
# mv = [[(0, 1), (1, 1)],
#       [(1, 0), (1, 1)],
#       [(0, 1), (1, 0), (1, 1)]]
#
# while que:
#     x, y, direction = que.popleft()
#
#     if x == n - 1 and y == n - 1:
#         answer += 1
#         continue
#
#     for i, dd in enumerate(mv[direction]):
#         nx, ny = x + dd[0], y + dd[1]
#
#         if 0 <= nx < n and 0 <= ny < n:
#             # 빈 칸이어야 하는 곳 확인
#             if maps[nx][ny] == 1:
#                 continue
#
#             if i == len(mv[direction]) - 1:
#                 if maps[nx - 1][ny] or maps[nx][ny - 1]:
#                     continue
#
#             # 다음 방향 결정
#             next_direction = 0
#
#             if direction == 0:
#                 next_direction = 0 if i == 0 else 2
#             elif direction == 1:
#                 next_direction = 1 if i == 0 else 2
#             else:
#                 next_direction = i
#
#             que.append((nx, ny, next_direction))

# print(answer)

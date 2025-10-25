N = int(input())

answer = 0
visited = [[False] * N for _ in range(N)]
down = [False] * N
# X-Y+N-1, X+Y
down_r, down_l = [False] * (2 * N-1), [False] * (2 * N-1)

def dfs(depth):
    global answer

    if depth == N:
        answer += 1
        return

    for col in range(N):
        if not down[col] and not down_r[depth-col+N-1] and not down_l[
            depth + col]:
            down[col] = down_r[depth-col+N-1] = down_l[depth+col] = True
            dfs(depth+1)
            down[col] = down_r[depth-col+N-1] = down_l[depth+col] = False

dfs(0)
print(answer)

"""
00 01 02
10 11 12
20 21 22
"""
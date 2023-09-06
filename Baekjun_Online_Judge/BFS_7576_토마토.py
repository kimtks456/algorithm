import sys

m, n = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
aged = [(i, j) for i in range(n) for j in range(m) if maps[i][j] == 1]
mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def aging(aged):
    next_aged = []

    while aged:
        x, y = aged.pop()

        for dx, dy in mv:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
                next_aged.append((nx, ny))
                maps[nx][ny] = 1

    return next_aged


def main():
    global aged
    if len(aged) == n * m:
        print(0)
        return

    days = 0

    while aged:
        '''
        이렇게 매번 다 익었는지 체크하니 시간초과남.
        따라서 그냥 days에서 1 빼줌
        '''
        # # 다 익었다면 종료
        # for row in maps:
        #     if 0 in row:
        #         break
        # else:
        #     print(days)
        #     return

        next_aged = aging(aged)
        days += 1
        aged += next_aged

        # print(aged)
        # for i in range(n):
        #     print(maps[i])
        # print()

    # 안익은 토마토 있는지 확인
    for row in maps:
        if 0 in row:
            print(-1)
            return

    print(days - 1)

main()
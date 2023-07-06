import sys
read = sys.stdin.readline


def main():
    dp = [[[False] * 21 for _ in range(21)] for _ in range(21)]

    while True:
        a, b, c = map(int, read().split())
        if a == b == c == -1:
            break
        result = w(a, b, c, dp)
        print(f'w({a}, {b}, {c}) = {result}')


def w(a, b, c, dp):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20, dp)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1, dp) + w(a, b - 1, c - 1, dp) - w(a, b - 1, c, dp)
        return dp[a][b][c]
    dp[a][b][c] = w(a - 1, b, c, dp) + w(a - 1, b - 1, c, dp) + w(a - 1, b, c - 1, dp) - w(a - 1, b - 1, c - 1, dp)
    return dp[a][b][c]


main()


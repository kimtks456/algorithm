import sys

read = sys.stdin.readline


def main():
    n = int(read())
    schedule = []
    dp = [0 for _ in range(n+1)]
    for _ in range(n):
        t, p = map(int, read().split())
        schedule.append([t, p])

    for i in range(n-1, -1, -1):
        if schedule[i][0] + i > n:
            dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[i+1], dp[i+schedule[i][0]] + schedule[i][1])

    print(dp[0])


main()

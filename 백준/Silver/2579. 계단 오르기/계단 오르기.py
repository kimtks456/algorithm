import sys
input = sys.stdin.readline


n = int(input())
stair = [int(input()) for _ in range(n)]

dp = [0] * n
if n < 3:
    print(sum(stair))
else:
    for i in range(2, n):
        dp[0], dp[1] = stair[0], stair[0] + stair[1]
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
    print(dp[n - 1])
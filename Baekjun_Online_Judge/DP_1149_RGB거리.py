import sys
input = sys.stdin.readline


n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
dp = [[] for _ in range(n)]

dp[0] = costs[0]
for i in range(1, n):
    temp = [0] * 3
    temp[0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    temp[1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    temp[2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
    dp[i] = temp

print(min(dp[n - 1]))

'''

R G R G R
R G B G B


3
26 10 83
49 5 57
13 89 99
= 31 + 13 = 44



'''
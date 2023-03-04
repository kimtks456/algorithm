import sys
import math


def solution(arr):
    answer = -1
    n = math.ceil(len(arr) / 2)

    min_dp = [[sys.maxsize for i in range(n)] for _ in range(n)]
    max_dp = [[-sys.maxsize for i in range(n)] for _ in range(n)]

    for i in range(n):
        min_dp[i][i], max_dp[i][i] = int(arr[i * 2]), int(arr[i * 2])

    for L in range(2, n + 1):
        for i in range(n - L + 1):  # n-1 - x + 1 = L
            j = L + i - 1  # j-i+1 = L
            for k in range(i, j):
                if arr[k * 2 + 1] == '+':
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                else:
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])

    answer = max_dp[0][n - 1]

    return answer

n = int(input())
children = list(map(int, input().split()))

dp = [0] * n
for ch in children:
    dp[ch - 1] = dp[ch - 2] + 1

# print(dp)
print(n - max(dp))

"""
5
3 1 2 4 5
"""
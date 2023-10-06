n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i - 1] = max(dp[i - 1], dp[j - 1] + 1)

print(max(dp))
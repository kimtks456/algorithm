n = int(input())
seq = list(map(int, input().split()))

# (이게 아님!!) i번째까지의 수들 중 가장 긴 증가 부분 수열의 길이
# i번째를 마지막으로 하는 가장 긴 증가 부분수열의 길이
dp = [1] * n

for i in range(n):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)


# print(dp)
print(max(dp))

"""
8
1 6 2 5 7 3 5 6

"""
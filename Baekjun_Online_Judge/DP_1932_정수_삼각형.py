import copy
import sys
input = sys.stdin.readline


n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

# Backtracking이 아니므로 visited에 추가해줄 필요 없음. 확인용으로 추가
answer = []
dp = [0] * 500
dp[0] = nums[0][0]
# visited = [[] for _ in range(500)]
# visited[0] = nums[0]

for depth in range(1, n):
    prev_dp = dp[:]
    # prev_visited = copy.deepcopy(visited)

    for j in range(depth + 1):
        if j == 0:
            dp[j] = prev_dp[j] + nums[depth][j]
            # visited[j].append(nums[depth][j])
            continue
        if j == depth:
            dp[j] = prev_dp[j - 1] + nums[depth][j]
            # visited[j] = prev_visited[j-1][:]
            # visited[j].append(nums[depth][j])
            continue

        left, right = prev_dp[j - 1], prev_dp[j]
        if left > right:
            dp[j] = left + nums[depth][j]
            # visited[j] = prev_visited[j-1][:]
            # visited[j].append(nums[depth][j])
        else:
            dp[j] = right + nums[depth][j]
            # visited[j] = prev_visited[j][:]
            # visited[j].append(nums[depth][j])


# print(visited[dp.index(max(dp))])
# print(sum(visited[dp.index(max(dp))]))
print(max(dp))
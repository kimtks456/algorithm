import sys
input = sys.stdin.readline


def solve2(start, temp):
    if start == N:
        if sum(temp) == S and len(temp) > 0:
            return 1
        return 0

    return solve2(start + 1, temp[:] + [nums[start]]) + solve2(start + 1, temp[:])


N, S = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

# print(solve(0, 0))
print(solve2(0, []))

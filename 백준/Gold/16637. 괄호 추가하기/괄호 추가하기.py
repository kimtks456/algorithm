from sys import stdin


def cal(a, b, op):
    a, b = map(int, [a, b])

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b


def solve(eq):
    if len(eq) == 1:
        return int(eq)

    max_dp = [0] * (len(eq) + 1)
    min_dp = [0] * (len(eq) + 1)
    max_dp[1], min_dp[1] = int(eq[0]), int(eq[0])
    max_dp[3], min_dp[3] = int(cal(eq[0], eq[2], eq[1])), int(cal(eq[0], eq[2], eq[1]))

    if len(eq) == 3:
        return max_dp[3]

    for i in range(5, len(eq) + 1, 2):
        max_dp[i] = max(
            cal(max_dp[i - 4], cal(eq[i - 3], eq[i - 1], eq[i - 2]), eq[i - 4]),
            cal(max_dp[i - 2], eq[i - 1], eq[i - 2]),
            cal(min_dp[i - 4], cal(eq[i - 3], eq[i - 1], eq[i - 2]), eq[i - 4]),
            cal(min_dp[i - 2], eq[i - 1], eq[i - 2])
        )
        min_dp[i] = min(
            cal(min_dp[i - 4], cal(eq[i - 3], eq[i - 1], eq[i - 2]), eq[i - 4]),
            cal(min_dp[i - 2], eq[i - 1], eq[i - 2]),
            cal(max_dp[i - 4], cal(eq[i - 3], eq[i - 1], eq[i - 2]), eq[i - 4]),
            cal(max_dp[i - 2], eq[i - 1], eq[i - 2])
        )

    return max_dp[len(eq)]


n = int(stdin.readline())
equation = stdin.readline().rstrip()

print(solve(equation))

"""
19
2*1-1*1+2*2-9*8-9*9

-> 189 나와야함. 음수 * 음수가 최대가 되는 경우도 고려해야함.
"""
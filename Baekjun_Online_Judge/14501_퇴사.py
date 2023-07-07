import sys

read = sys.stdin.readline


def main():
    n = int(read())
    schedule = []
    for _ in range(n):
        t, p = map(int, read().split())
        schedule.append([t, p])

    max_profit = 0
    for i in range(n):
        temp_profit = dp(schedule, i, 0)
        if temp_profit > max_profit:
            max_profit = temp_profit

    print(max_profit)


def dp(schedule, start_idx, profit):
    if start_idx + schedule[start_idx][0] > len(schedule):
        return profit
    if start_idx + schedule[start_idx][0] == len(schedule):
        return profit + schedule[start_idx][1]

    return max(dp(schedule, start_idx + schedule[start_idx][0], profit + schedule[start_idx][1]),
               dp(schedule, start_idx + 1, profit))


main()

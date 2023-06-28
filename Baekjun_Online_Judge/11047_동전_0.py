import sys
read = sys.stdin.readline


def main():
    n, k = map(int, read().split())
    coins = [int(read()) for _ in range(n)]
    answer = 0

    for cost in reversed(coins):
        if cost > k:
            continue
        temp = k // cost
        k -= temp * cost
        answer += temp
        if cost == 0:
            break

    print(answer)


main()
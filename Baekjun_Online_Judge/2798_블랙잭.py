import sys
read = sys.stdin.readline
from itertools import combinations


def main():
    n, m = map(int, read().split())
    cards = list(map(int, read().split()))
    cases = list(combinations(cards, 3))
    answer = 0

    for n1, n2, n3 in cases:
        # sum = cards[n1-1] + cards[n2-1] + cards[n3-1]
        sum = n1 + n2 + n3
        if sum == m:
            print(sum)
            return 0
        if sum > m:
            continue
        if answer < sum:
            answer = sum

    print(answer)

main()
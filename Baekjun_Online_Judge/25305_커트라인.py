import sys
read = sys.stdin.readline


def main():
    n, k = map(int, read().split())
    scores = list(map(int, read().split()))
    scores.sort()

    print(scores[n-k])

main()
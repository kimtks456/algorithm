import sys


def main():
    n = int(input())
    waiting = list(map(int, sys.stdin.readline().split()))
    waiting.sort()
    time = [sum(waiting[:i]) for i in range(1, len(waiting) + 1)]

    print(sum(time))

main()
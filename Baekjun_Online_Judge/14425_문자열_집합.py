import sys
read = sys.stdin.readline


def main():
    n, m = map(int, read().split())
    target = set()
    for _ in range(n):
        target.add(read().rstrip())

    answer = 0
    for _ in range(m):
        temp = read().rstrip()
        if temp in target:
            answer += 1

    print(answer)


main()
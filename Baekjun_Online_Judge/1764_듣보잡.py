import sys
read = sys.stdin.readline


def main():
    n, m = map(int, read().split())
    seen, heard = set(), set()
    for _ in range(n):
        seen.add(read().strip())
    for _ in range(m):
        heard.add(read().strip())

    answer = seen.intersection(heard)

    print(len(answer))
    for item in sorted(list(answer)):
        print(item)


main()
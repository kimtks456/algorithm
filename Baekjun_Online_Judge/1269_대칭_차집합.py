import sys
read = sys.stdin.readline


def main():
    n, m = map(int, read().split())
    a = set(map(int, read().split()))
    b = set(map(int, read().split()))
    print(len(a.difference(b)) + len(b.difference(a)))

main()
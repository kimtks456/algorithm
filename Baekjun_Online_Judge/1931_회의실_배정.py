import sys
read = sys.stdin.readline


def main():
    n = int(read())
    cases = []
    for _ in range(n):
        start, stop = map(int, read().split())
        cases.append((start, stop))

    cases.sort(key=lambda x: (x[1], x[0]))
    prev = 0
    cnt = 0
    for start, stop in cases:
        if prev > start:
            continue
        cnt += 1
        prev = stop

    print(cnt)


main()
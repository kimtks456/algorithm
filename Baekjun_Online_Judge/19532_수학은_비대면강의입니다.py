import sys
read = sys.stdin.readline


def main():
    a, b, c, d, e, f = map(int, read().split())
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a*x + b*y == c:
                if d*x + e*y == f:
                    print(x, y)
                    return 0

main()

import sys
read = sys.stdin.readline


def main():
    n = int(read())

    if n % 5 == 0:
        return int(n/5)

    numberOfThree = [i * 3 for i in range(1, int(n/3) + 1)]

    for num in numberOfThree:
        if (n - num) % 5 == 0:
            return int(num / 3) + int((n - num) / 5)
    return -1


print(main())
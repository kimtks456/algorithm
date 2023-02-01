import sys

read = sys.stdin.readline


def main():
    n = int(read())
    result = n % 100

    if n >= 100:
        result = 99
        for i in range(100, n + 1):
            if int(i / 100) - int((i % 100) / 10) == int((i % 100) / 10) - int(i % 10):
                result += 1
    print(result)
    return result


main()

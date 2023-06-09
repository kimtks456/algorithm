import sys
read = sys.stdin.readline


def main():
    n = int(read())
    having = list(map(int, read().split()))

    m = int(read())
    target = list(map(int, read().split()))

    count = dict()
    for item in having:
        if item in count.keys():
            count[item] += 1
        else:
            count[item] = 1

    for now in target:
        if now in count.keys():
            print(count[now], end=' ')
        else:
            print(0, end=' ')

main()
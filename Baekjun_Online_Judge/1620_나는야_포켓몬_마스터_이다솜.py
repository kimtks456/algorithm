import sys
read = sys.stdin.readline


def main():
    n, m = map(int, read().split())
    names = []
    order = dict()
    for i in range(n):
        temp = read().strip()
        names.append(temp)
        order[temp] = i

    for _ in range(m):
        temp = read().strip()
        if temp.isdigit():
            print(names[int(temp) - 1])
        else:
            print(order[temp] + 1)


main()
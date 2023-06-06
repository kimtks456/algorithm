import sys
read = sys.stdin.readline


def main():
    n = int(read())
    members = [(list(read().split()), i) for i in range(n)]
    members.sort(key=lambda x: (int(x[0][0]), x[1]))

    for i in range(n):
        print(members[i][0][0], members[i][0][1])


main()
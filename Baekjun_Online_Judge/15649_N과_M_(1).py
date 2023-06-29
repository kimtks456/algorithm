import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    dfs([], n, m)

def dfs(s, n, m):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs(s, n, m)
            s.pop()


main()
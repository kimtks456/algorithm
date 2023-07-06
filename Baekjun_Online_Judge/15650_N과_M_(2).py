def main():
    n, m = map(int, input().split())
    dfs(1, [], n, m)


def dfs(start, s, n, m):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(i + 1, s, n, m)
        s.pop()


main()
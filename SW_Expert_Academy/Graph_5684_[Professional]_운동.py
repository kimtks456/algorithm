from collections import deque


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    # Edge Map 만들기
    maps = dict()
    for _ in range(m):
        s, e, c = map(int, input().split())
        if s not in maps.keys():
            maps[s] = [(e, c)]
        else:
            maps[s].append((e, c))

    # 모든 점에 대해 cycle 탐지
    min_cycle = 10000 * n * (n-1)
    for v in range(1, n + 1):

        # bfs
        que = deque([(v, 0)])
        visited = set([v])

        while que:
            s, length = que.popleft()

            if s not in maps.keys():
                continue

            for e, c in maps[s]:
                if e == v:
                    min_cycle = min(min_cycle, length + c)
                    break
                if e not in visited:
                    que.append((e, length + c))
                    visited.add(e)

    if min_cycle == 10000 * n * (n-1):
        min_cycle = -1

    print(f"#{test_case} {min_cycle}")

"""
2
2 2
1 2 1
1 2 1
2 3
1 2 1
2 1 2
1 2 3

-> -1, 3




"""
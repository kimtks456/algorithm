from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(start):
    que = []
    heappush(que, (0, start))

    while que:
        now_w, s = heappop(que)

        # 최단거리가 갱신되어 더 작아졌다면, 더 돌릴 필요 없음
        # 더이상 최단 거리가 아니니까
        if now_w > sp[s]:
            continue

        for v, w in graph[s]:
            if now_w + w < sp[v]:
                sp[v] = now_w + w
                heappush(que, (now_w + w, v))


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
INF = 10 ** 9
sp = [INF] * (V + 1)
sp[K] = 0

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

dijkstra(K)

for i in range(1, V + 1):
    print(sp[i] if sp[i] != INF else "INF")
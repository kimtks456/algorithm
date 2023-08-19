import sys
from collections import deque


n, m, start = map(int, input().split())
edge = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# Build Graph
graph = [[] for _ in range(n)]
for s, e in edge:
    if s not in graph[e-1]:
        graph[e-1].append(s)
    if e not in graph[s-1]:
        graph[s-1].append(e)

# DFS
stack = [start]
visited = []
answer_dfs = []
while stack:
    now = stack.pop()

    if now in visited:
        continue
    answer_dfs.append(now)

    for i in sorted(graph[now-1], reverse=True):
        if i not in visited:
            stack.append(i)
    visited.append(now)

# BFS
queue = deque()
queue.append(start)

visited = []
answer_bfs = []
while queue:
    now = queue.popleft()

    if now in visited:
        continue
    answer_bfs.append(now)

    for i in sorted(graph[now-1]):
        if i not in visited:
            queue.append(i)
    visited.append(now)


# Answer Output
for i in range(len(answer_dfs)):
    print(answer_dfs[i], end=' ')
print()
for i in range(len(answer_bfs)):
    print(answer_bfs[i], end=' ')
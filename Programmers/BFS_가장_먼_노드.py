from collections import deque


def solution(n, edge):
    answer = 0
    adj = [[] for i in range(n + 1)]
    # 노드 1부터 봐야하니. 근데 안해도 통과 되긴 함
    # edge.sort()

    for i, j in edge:
        adj[i].append(j)
        adj[j].append(i)

    q = deque()
    visited = [0] * (n + 1)
    q.append(1)
    visited[1] = 1

    while q:
        start = q.popleft()

        for i in adj[start]:
            if visited[i] == 0:
                visited[i] = 1 + visited[start]
                q.append(i)

    maxDist = max(visited)
    for i in visited:
        if i == maxDist:
            answer += 1

    return answer
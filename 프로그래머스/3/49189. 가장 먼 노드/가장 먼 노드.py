from collections import deque


def solution(n, edge):
    answer = 0
    max_path = 0
    
    # build graph
    graph = [set() for _ in range(n+1)]
    for u, v in edge:
        graph[u].add(v)
        graph[v].add(u)
    
    visited = [False] * (n + 1)
    visited[1] = True
    que = deque([(1, 0)]) # (node #, path length)
    
    while que:
        node, path = que.popleft()
        # print(f'node:{node}, path:{path}')
        # for row in visited:
        #     print(visited)
        
        for next_node in graph[node]:
            if not visited[next_node]:
                que.append((next_node, path + 1))
                visited[next_node] = True
        else:
            if path > max_path:
                answer = 1
                max_path = path
            elif path == max_path:
                answer += 1
    
    return answer


# from collections import deque
# 
# 
# def solution(n, edge):
#     answer = 0
#     adj = [[] for i in range(n+1)]
#     # 노드 1부터 봐야하니
#     # edge.sort()
#     
#     for i, j in edge:
#         adj[i].append(j)
#         adj[j].append(i)
#         
#     q = deque()
#     visited = [0] * (n+1)
#     q.append(1)
#     visited[1] = 1
#     
#     while q:
#         start= q.popleft()
#         
#         for i in adj[start]:
#             if visited[i] == 0:
#                 visited[i] = 1 + visited[start]
#                 q.append(i)
#                 
#     maxDist = max(visited)
#     for i in visited:
#         if i == maxDist:
#             answer += 1
#             
#     return answer
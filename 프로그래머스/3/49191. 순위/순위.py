from collections import defaultdict

def solution(n, results):
    answer = 0
    
    graph = [[0] * (n+1) for _ in range(n+1)]
    for u, v in results:
        graph[u][v] = 1
        graph[v][u] = -1
    
    # Floyd-Warshall
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                temp = graph[i][k] + graph[k][j]
                #a, b = graph[i][k], graph[k][j]
                if temp == 2:
                #if a == 1 and b == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
                elif temp == -2:
                #if a == -1 and b == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1
    
    for row in graph:
        temp = sum([i != 0 for i in row])
        answer += temp == n - 1
    
    return answer
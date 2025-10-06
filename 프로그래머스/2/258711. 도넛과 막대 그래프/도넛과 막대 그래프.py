from collections import defaultdict

def solution(edges):
    answer = [0] * 4
    
    # graph 생성
    adj = defaultdict(set)
    for v1, v2 in edges:
        adj[v1].add(v2)
        
    # 시작점 찾기: 나가는거 1개 이상, 들어오는 edge 없음
    candidate = set(adj.keys())
    max_deg_set, max_deg = set(), 0 # 나가는거 최대인 vertex, deg
    for v, to_set in adj.items():
        candidate -= to_set
        if max_deg < len(to_set):
            max_deg_set, max_deg = set([v]), len(to_set)
        elif max_deg == len(to_set):
            max_deg_set.add(v)
    answer[0] = list(candidate & max_deg_set)[0]
        
    def dfs(start):
        stack = [(start, 0)]
        visited = set([start])
        # 각 노드별 나가는 edge 개수
        degree = 0
        
        while stack:
            now, depth = stack.pop()
            degree = max(degree, len(adj[now]))
            
            # 8자 모양 = 3
            if degree == 2:
                return 3
                
            # 막대인 경우 = 2
            if len(adj[now]) == 0:
                return 2
            
            for nxt in adj[now]:
                if not nxt in visited:
                    stack.append((nxt, depth + 1))
                    visited.add(nxt)
        
        # 도넛 모양 = 1
        if degree == 1:
            return 1 
        else:
            print('ERROR, degree = ', degree)
            return -1
    
    for node in adj[answer[0]]:
        result = dfs(node)
        answer[result] += 1
    
    return answer

def solution(tickets):
    n = len(tickets)
    answer = []
    
    # 오름차순으로 경로 선택
    tickets.sort()
    
    # ticket은 한번씩 사용
    visited = [False] * n
    
    def search(start, path):
        nonlocal answer 
        
        if len(path) == n + 1:
            answer = path
            return True
        
        for i, ticket in enumerate(tickets):
            if not visited[i] and ticket[0] == start:
                visited[i] = True
                if search(ticket[1], path[:] + [ticket[1]]):
                    return True
                visited[i] = False
        return False
    
    search('ICN', ['ICN'])
        
    return answer
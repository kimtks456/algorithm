from collections import deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    visited = [[False] * m for _ in range(n)]
    que = deque()
    que.append((0, 0, 1))
    visited[0][0] = True
    
    while que:
        # print(que)
        # for row in visited:
        #     print(row)
        y, x, path = que.popleft()
        
        if (y, x) == (n-1, m-1):
            answer = path
            break
        
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1 and not visited[ny][nx]:
                que.append((ny, nx, path + 1))
                visited[ny][nx] = True
    
    return answer



# from collections import deque
# 
# def solution(maps):
#     answer = 1
#     q = deque()
#     n, m = len(maps), len(maps[0])
#     visited = [[False for _ in range(m)] for _ in range(n)]
#     move = [(-1,0), (1,0), (0,-1), (0,1)]
#     
#     q.append((0,0,answer))
#     visited[0][0] = True
#     temp = 1
#     
#     while q:
#         x, y, temp = q.popleft()
#         
#         if x == n-1 and y == m-1:
#             answer = temp
#             break
#         
#         for mx, my in move:
#             nx, ny = x + mx, y + my
#             if 0 <= nx <= n-1 and 0 <= ny <= m-1 and visited[nx][ny] is False and maps[nx][ny] == 1:
#                 q.append((nx, ny, temp + 1))
#                 visited[nx][ny] = True
#                 
#     if x != n-1 or y != m-1:
#         answer = -1
#     
#     return answer
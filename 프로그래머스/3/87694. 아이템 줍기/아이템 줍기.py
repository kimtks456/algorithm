from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 이동 가능 좌표 = 1, 그 외는 0으로 지도 초기화
    item_map = [[-1] * 102 for _ in range(102)]
    for rec in rectangle:
        # 좌표값 2배하여 ㄷ 케이스 식별
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                if y1 < i < y2 and x1 < j < x2:
                    # 직사각형 내부 = 0
                    item_map[i][j] = 0
                elif item_map[i][j] != 0:
                    # 다른 직사각형의 내부 아니면서 테두리인 경우 = 1
                    item_map[i][j] = 1
    
    dd = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    q = deque()
    q.append((characterX * 2, characterY * 2, 0))
    visited = [[False] * 102 for _ in range(102)]
    visited[characterY*2][characterX*2] = True
    
    while q:
        x, y, dist = q.popleft()
        
        if x == itemX * 2 and y == itemY * 2:
            answer = dist // 2
            break
        
        for dx, dy in dd:
            nx, ny = x + dx, y + dy
            if item_map[ny][nx] == 1 and not visited[ny][nx]:
                q.append((nx, ny, dist + 1))
                visited[ny][nx] = True
    
    return answer
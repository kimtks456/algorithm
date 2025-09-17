from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def roll(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
        if board[x][y] == 'O':
            break
    return x, y, cnt

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visited = set()
    visited.add((rx, ry, bx, by))

    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth >= 10:
            return -1

        for dx, dy in dirs:
            nrx, nry, rcnt = roll(rx, ry, dx, dy)
            nbx, nby, bcnt = roll(bx, by, dx, dy)

            if board[nbx][nby] == 'O':  # 파란 공 빠지면 실패
                continue
            if board[nrx][nry] == 'O':  # 빨간 공만 빠지면 성공
                return depth + 1

            # 겹침 처리
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth + 1))
    return -1

print(bfs(rx, ry, bx, by))


# from collections import deque
#
#
# # 90도 시계방향 회전
# def rotate90(arr):
#     n, m = len(arr), len(arr[0])
#     rotated = [[0 for _ in range(n)] for _ in range(m)]
#     rx, ry, bx, by = 0, 0, 0, 0
#
#     for i in range(n):
#         for j in range(m):
#             rotated[j][n - 1 - i] = arr[i][j]
#             if arr[i][j] == 'R':
#                 rx, ry = n - 1 - i, j
#             elif arr[i][j] == 'B':
#                 bx, by = n - 1 - i, j
#
#     return (rx, ry, bx, by, rotated)
#
# # 오른쪽 이동
# def move_right(x, y, board, is_red):
#     while x + 1 <= len(board[0]) and board[y][x + 1] not in ('R', 'B', '#'):
#         if board[y][x + 1] == 'O':
#             if is_red:
#                 return 1
#             else:
#                 return -1
#         if board[y][x + 1] == '.':
#             board[y][x + 1] = 'R' if is_red else 'B'
#             board[y][x] = '.'
#             x += 1
#
#     return 0
#
# # 오른쪽 이동: 1=게임성공, -1=게임실패, 0=정상
# def move(rx, ry, bx, by, board):
#     # 오른쪽에 있는 구슬 먼저 진행
#     if ry == rx and rx > bx:
#         result1 = move_right(rx, ry, board, True)
#         if result1 in (1, -1):
#             return result1
#         result2 = move_right(bx, by, board, False)
#         if result2 in (1, -1):
#             return result2
#     else:
#         result2 = move_right(bx, by, board, False)
#         if result2 in (1, -1):
#             return result2
#         result1 = move_right(rx, ry, board, True)
#         if result1 in (1, -1):
#             return result1
#
#     return 0
#
#
# # BFS
# def bfs(data):
#     que = deque([data])
#     print(que)
#     # sleep(1)
#     visited = set()
#
#     while que:
#         count, board = que.popleft()
#         print(count, board)
#
#         if count > 10:
#             return -1
#
#         for _ in range(4):
#             rrx, rry, rbx, rby, board = rotate90(board)
#             copy = [row[:] for row in board]
#
#             result = move(rrx, rry, rbx, rby, copy)
#             if result == 1:
#                 return count + 1
#             elif result == 0:
#                 que.append((count + 1, copy))
#
#     return -1
#
# # 풀이
# n, m = map(int, input().split())
# board = [list(input()) for _ in range(n)]
# for i, row in enumerate(board):
#     for j, item in enumerate(row):
#         if item == 'R':
#             rx, ry = i, j
#         elif item == 'B':
#             bx, by = i, j
# """
# 5 5
# #####
# #O.B#
# #.#.#
# #RO.#
# #####
# """
# answer = bfs((0, board))
# print('answer : ', answer)
# # rx, ry, bx, by, board = rotate90(board)
# # [print(''.join(row)) for row in board]
# # result = move_right(1,1, board, True)
# # print(result)
# #
# # [print(''.join(row)) for row in board]

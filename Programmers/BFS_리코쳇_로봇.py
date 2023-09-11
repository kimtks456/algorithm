from collections import deque


def solution(board):
    answer = 0
    start, end = (), ()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start = (i, j)
            if board[i][j] == 'G':
                end = (i, j)

    def move(maps, start, mv):
        # 상
        if mv == 0:
            if start[0] == 0:
                return start
            idx = -1
            while True:
                temp = idx + start[0]
                if maps[temp][start[1]] == 'D':
                    return (temp + 1, start[1])
                if temp == 0:
                    return (temp, start[1])
                idx -= 1

        # 하
        if mv == 2:
            if start[0] == len(maps) - 1:
                return start
            idx = 1
            while True:
                temp = idx + start[0]
                if maps[temp][start[1]] == 'D':
                    return (temp - 1, start[1])
                if temp == len(maps) - 1:
                    return (temp, start[1])
                idx += 1

        # 우
        if mv == 1:
            if start[1] == len(maps[0]) - 1:
                return start
            idx = 1
            while True:
                temp = idx + start[1]
                if maps[start[0]][temp] == 'D':
                    return (start[0], temp - 1)
                if temp == len(maps[0]) - 1:
                    return (start[0], temp)
                idx += 1

        # 좌
        if mv == 3:
            if start[1] == 0:
                return start
            idx = -1
            while True:
                temp = idx + start[1]
                if maps[start[0]][temp] == 'D':
                    return (start[0], temp + 1)
                if temp == 0:
                    return (start[0], temp)
                idx -= 1

    # BFS
    visited = set()
    visited.add(start)
    que = deque([(start[0], start[1], 0)])

    while que:
        x, y, v = que.popleft()

        if x == end[0] and y == end[1]:
            return v

        for i in range(4):
            target = move(board, (x, y), i)
            if target not in visited:
                visited.add(target)
                que.append((target[0], target[1], v + 1))
    else:
        return -1


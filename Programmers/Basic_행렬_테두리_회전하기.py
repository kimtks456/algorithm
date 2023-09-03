def rotate(maps, query):
    x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
    min_value = 10001

    # up
    temp_up_right = maps[x1][y2]
    for i in range(y2, y1, -1):
        maps[x1][i] = maps[x1][i - 1]

    # right
    temp_down_right = maps[x2][y2]
    for j in range(x2, x1, -1):
        maps[j][y2] = maps[j - 1][y2]
    maps[x1 + 1][y2] = temp_up_right

    # down
    temp_down_left = maps[x2][y1]
    for i in range(y1, y2):
        maps[x2][i] = maps[x2][i + 1]
    maps[x2][y2 - 1] = temp_down_right

    # left
    for j in range(x1, x2):
        maps[j][y1] = maps[j + 1][y1]
    maps[x2 - 1][y1] = temp_down_left

    return maps, min(min(maps[x1][y1:y2 + 1]), min(maps[x2][y1:y2 + 1]),
                     min([maps[i][y2] for i in range(x1, x2 + 1)]),
                     min([maps[i][y1] for i in range(x1, x2 + 1)]))


def solution(rows, columns, queries):
    answer = []
    maps = [[1 + i + j * columns for i in range(columns)] for j in range(rows)]
    temp_min = 10001
    for i in queries:
        maps, temp_min = rotate(maps, i)
        answer.append(temp_min)

    return answer
import sys
import copy


answer = 64
def main():
    n, m = map(int, sys.stdin.readline().split())
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    case = [[] for _ in range(5)]

    for i in range(n):
        for j in range(m):
            temp = maps[i][j]
            if temp != 6 and temp != 0:
                case[temp - 1].append((i, j, 0))
    conv2cctv_map(n, m, maps, case, 0)
    print(answer)


def conv2cctv_map(n, m, maps, case, target_switch_case):
    if target_switch_case == 5:
        global answer
        temp = count_blind_spot(maps)
        answer = min(temp, answer)
        return

    if len(case[target_switch_case]) == 0:
        conv2cctv_map(n, m, maps, case, target_switch_case + 1)
        return

    i, j, direction = case[target_switch_case].pop(0)

    for k in range(4):
        direction += k
        backup = copy.deepcopy(maps)

        if target_switch_case == 0:
            if direction % 4 == 0:
                rightward(maps, i, j, m)
            elif direction % 4 == 1:
                downward(maps, i, j, n)
            elif direction % 4 == 2:
                leftward(maps, i, j)
            else:
                upward(maps, i, j)

        elif target_switch_case == 1:
            if direction % 4 == 0:
                rightward(maps, i, j, m)
                leftward(maps, i, j)
            else:
                upward(maps, i, j)
                downward(maps, i, j, n)

        elif target_switch_case == 2:
            if direction % 4 == 0:
                upward(maps, i, j)
                rightward(maps, i, j, m)
            elif direction % 4 == 1:
                rightward(maps, i, j, m)
                downward(maps, i, j, n)
            elif direction % 4 == 2:
                downward(maps, i, j, n)
                leftward(maps, i, j)
            else:
                leftward(maps, i, j)
                upward(maps, i, j)

        elif target_switch_case == 3:
            if direction % 4 == 0:
                leftward(maps, i, j)
                upward(maps, i, j)
                rightward(maps, i, j, m)
            elif direction % 4 == 1:
                upward(maps, i, j)
                rightward(maps, i, j, m)
                downward(maps, i, j, n)
            elif direction % 4 == 2:
                rightward(maps, i, j, m)
                downward(maps, i, j, n)
                leftward(maps, i, j)
            else:
                downward(maps, i, j, n)
                leftward(maps, i, j)
                upward(maps, i, j)

        else:
            rightward(maps, i, j, m)
            downward(maps, i, j, n)
            leftward(maps, i, j)
            upward(maps, i, j)

        # for x in range(n):
        #     for y in range(m):
        #         print(maps[x][y], end=' ')
        #     print()

        conv2cctv_map(n, m, maps, copy.deepcopy(case), target_switch_case)
        maps = copy.deepcopy(backup)


def rightward(maps, i, j, m):
    right = 1
    while j + right < m and maps[i][j + right] != 6:
        if maps[i][j + right] == 0:
            maps[i][j + right] = '#'
        right += 1


def downward(maps, i, j, n):
    down = 1
    while i + down < n and maps[i + down][j] != 6:
        if maps[i + down][j] == 0:
            maps[i + down][j] = '#'
        down += 1


def upward(maps, i, j):
    up = 1
    while -1 < i - up and maps[i - up][j] != 6:
        if maps[i - up][j] == 0:
            maps[i - up][j] = '#'
        up += 1


def leftward(maps, i, j):
    left = 1
    while -1 < j - left and maps[i][j - left] != 6:
        if maps[i][j - left] == 0:
            maps[i][j - left] = '#'
        left += 1


def count_blind_spot(maps):
    count = 0
    for row in maps:
        for item in row:
            if item == 0:
                count += 1
    return count


main()

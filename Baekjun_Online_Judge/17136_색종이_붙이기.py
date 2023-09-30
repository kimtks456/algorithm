import sys


def find_max_paper(maps, start):
    x, y = start
    d = 5

    while d > 0:
        if x + d > 10 or y + d > 10:
            d -= 1
            continue
        for i in range(x, x + d):
            flag = True
            for j in range(y, y + d):
                if maps[i][j] == 0:
                    flag = False
                    break
            if flag is False:
                break
        if flag is False:
            d -= 1
        else:
            return d


# 1이 없다면 True
def check_all_zero():
    flag = True
    i = 0
    while flag and i in range(10):
        j = 0
        while flag and j in range(10):
            if maps[i][j] == 1:
                flag = False
            j += 1
        i += 1
    return flag


def solve(count):
    global answer
    flag = True

    i = 0
    while flag and i in range(10):
        j = 0
        while flag and j in range(10):
            if maps[i][j] == 0:
                j += 1
                continue

            d = find_max_paper(maps, (i, j))
            # print(i, j, d, papers)
            # for row in maps:
            #     print(row)
            # print()
            while d > 0:
                if papers[d - 1] == 0:
                    d -= 1
                    continue

                papers[d - 1] -= 1
                for ii in range(i, i + d):
                    for jj in range(j, j + d):
                        maps[ii][jj] = 0

                solve(count + 1)

                papers[d - 1] += 1
                for ii in range(i, i + d):
                    for jj in range(j, j + d):
                        maps[ii][jj] = 1

                d -= 1
            flag = False
        i += 1

    if check_all_zero():
        answer = min(answer, count)


maps = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]

answer, papers = 26, [5] * 5

solve(0)

if answer == 26:
    print(-1)
else:
    print(answer)

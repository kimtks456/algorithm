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


def solve(maps, papers):
    # 1이 없다면 종료
    flag = False
    for i in range(10):
        for j in range(10):
            if maps[i][j] == 1:
                flag = True
    if flag is False:
        return 25 - sum(papers), papers

    # 1이 있는데 paper를 다 썼다면 종료
    if papers == [0] * 5 and flag is True:
        return 26, papers

    global result
    result_papers = []
    for i in range(10):
        for j in range(10):
            if maps[i][j] == 1:
                d = find_max_paper(maps, (i, j))
                # print("now i, j, d : ", i, j, d)
                # print("papers : ", papers)
                # for row in maps:
                #     print(row)
                # print()
                while d > 0:
                    # 해당 paper가 없으면 다음 색종이로 넘어가기
                    if papers[d - 1] == 0:
                        if d == 1:
                            return 26, result_papers
                        d -= 1
                        continue

                    # 색종이 붙이기
                    for ii in range(i, i + d):
                        for jj in range(j, j + d):
                            maps[ii][jj] = 0
                    papers[d - 1] -= 1

                    # 1이 없다면 종료
                    flag2 = False
                    for ii in range(10):
                        for jj in range(10):
                            if maps[ii][jj] == 1:
                                flag2 = True
                    if flag2 is False:
                        # print("no ones")
                        # for row in maps:
                        #     print(row)
                        # print(papers)
                        return 25 - sum(papers), papers

                    temp_result1, result_papers = solve(maps, papers)

                    # 색종이 다시 떼기
                    for ii in range(i, i + d):
                        for jj in range(j, j + d):
                            maps[ii][jj] = 1
                    papers[d - 1] += 1

                    result = min(result, temp_result1)
                    d -= 1
    # print("final : ", result, result_papers)
    return result, result_papers


maps = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]

result = 0
answer, papers = solve(maps, [5] * 5)
if answer == 26:
    print(-1)
else:
    print(answer)

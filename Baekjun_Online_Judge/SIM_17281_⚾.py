import sys


def permutation(arr, r):
    result = []
    visited = [False] * len(arr)

    def dfs(case):
        if len(case) == r:
            result.append(case[:])
            return

        for i, v in enumerate(arr):
            if visited[i]:
                continue

            case.append(v)
            visited[i] = True
            dfs(case)

            case.pop()
            visited[i] = False

    dfs([])
    return result


def solve():
    score = 0

    for case in cases:
        temp_score = 0
        case = case[:3] + [0] + case[3:]
        # if case == [1, 2, 3, 0, 4, 5, 6, 7, 8]:
        #     print("now")
        #     break
        hitter_idx = 0
        for inning in innings:
            out = 0
            b1, b2, b3 = 0, 0, 0
            while out < 3:
                if inning[case[hitter_idx]] == 0:
                    out += 1
                elif inning[case[hitter_idx]] == 1:
                    temp_score += b3
                    b1, b2, b3 = 1, b1, b2
                elif inning[case[hitter_idx]] == 2:
                    temp_score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif inning[case[hitter_idx]] == 3:
                    temp_score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                else:
                    temp_score += b1 + b2 + b3 + 1
                    b1, b2, b3 = 0, 0, 0

                hitter_idx = (hitter_idx + 1) % 9
                # print("inning : ", inning)
                # print(hitter_idx, temp_score, base, out)
                # print()
        score = max(score, temp_score)

    return score


n = int(sys.stdin.readline())
innings = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cases = permutation([i for i in range(1, 9)], 8)
# cases = [[1, 2, 3, 4, 5, 6, 7, 8]]
answer = solve()

print(answer)


"""
50
1 2 4 3 0 2 1 0 3
1 2 1 2 0 0 0 0 1
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 0
0 2 0 3 0 1 0 2 0
1 2 4 3 0 2 1 0 3
1 2 1 2 0 0 0 0 1
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 0
0 2 0 3 0 1 0 2 0
1 2 4 3 0 2 1 0 3
1 2 1 2 0 0 0 0 1
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 0
0 2 0 3 0 1 0 2 0
1 2 4 3 0 2 1 0 3
1 2 1 2 0 0 0 0 1
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 0
0 2 0 3 0 1 0 2 0
1 2 4 3 0 2 1 0 3
1 2 1 2 0 0 0 0 1
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 0
0 2 0 3 0 1 0 2 0
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2

이 코드의 출력: 766

올바른 출력: 500

"""
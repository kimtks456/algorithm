def solution(m, n, puddles):
    answer = 0
    count = [[0 for _ in range(m)] for _ in range(n)]
    count[0][0] = 1

    # Mark puddles
    for i, j in puddles:
        count[j - 1][i - 1] = -1

    for i in range(m):
        for j in range(n):

            if count[j][i] == -1:
                continue
            up, left = 0, 0
            if 0 <= j - 1 and count[j - 1][i] != -1:
                up = count[j - 1][i]
            if 0 <= i - 1 and count[j][i - 1] != -1:
                left = count[j][i - 1]
            count[j][i] += up + left

    answer = count[n - 1][m - 1] % 1000000007
    return answer


print(solution(4, 3, [[2, 2]]))
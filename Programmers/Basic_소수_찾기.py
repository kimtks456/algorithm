def solution(n):
    answer = 0
    check = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if check[i]:
            answer += 1
            for j in range(2 * i, n + 1, i):
                check[j] = False

    return answer
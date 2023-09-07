import sys

def generate_pascal(r):
    if r == 1:
        return [1]

    i, result = 2, [1, 1]
    while i < r:
        temp = []
        for j in range(len(result) + 1):
            if j == 0:
                temp = [1]
                continue
            if j == len(result):
                temp.append(1)
                continue
            temp.append(result[j - 1] + result[j])

        result = temp
        i += 1
    return result


def permutation(arr, r):
    visited = [False] * len(arr)

    def dfs(chosen):
        global answer
        if len(chosen) == r:
            result = 0
            for i in range(r):
                result += chosen[i] * pascal_num[i]

            if result == f:
                for i in range(r):
                    print(chosen[i], end=' ')
                sys.exit(0)
                answer.append(chosen[:])
            return

        for i, v in enumerate(arr):
            if visited[i]:
                continue
            chosen.append(arr[i])
            visited[i] = True
            dfs(chosen)

            chosen.pop()
            visited[i] = False

    dfs([])


n, f = map(int, input().split())
answer = []

pascal_num = generate_pascal(n)
permutation([i + 1 for i in range(n)], n)
# print(answer)
# answer = sorted(answer)[0]
# for i in range(len(answer)):
#     print(answer[i], end=' ')

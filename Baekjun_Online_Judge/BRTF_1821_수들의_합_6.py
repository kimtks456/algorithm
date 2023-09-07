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

'''
DP 풀이
https://janghan-kor.tistory.com/784

import sys

def dfs(idx, result):
    global finish
    if finish or result > sum:
        return
    if idx == N:
        if sum == result:
            for i in range(N):
                print(ans[i], end=" ")
            finish = True
        return
    for i in range(1, N+1):
        if not check[i]:
            check[i] = True
            ans[idx] = i
            dfs(idx+1, result + mul[idx] * i)
            if finish:
                break
            check[i] = False

N, sum = map(int, sys.stdin.readline().split())

factorial = [0] * N
mul = [0] * N
check = [False] * (N+1)
ans = [0] * N
factorial[0] = 1
for i in range(1, N):
    factorial[i] = factorial[i-1] * i

for i in range(N):
    mul[i] = factorial[N - 1] // (factorial[N - 1 - i] * factorial[i])
finish = False
dfs(0, 0)

'''


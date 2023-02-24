from collections import deque


def solution(n, computers):
    answer = n
    visited = [0] * n

    q = deque([0])
    visited[0] = 1

    while q:
        now = q.popleft()
        print("now : ", now)

        for i in range(n):
            if now == i:
                continue

            if visited[i] != 1:
                q.append(i)

            if visited[i] != 1 and computers[now][i] == 1:
                print("visit : " , visited[i])
                print("i " ,i)
                answer -= 1

        visited[now] = 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
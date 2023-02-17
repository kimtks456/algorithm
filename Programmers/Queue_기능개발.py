from collections import deque
from math import ceil


def solution(progresses, speeds):
    answer = []
    que = deque()

    for i in range(len(progresses)):
        que.append(ceil((100 - progresses[i]) / speeds[i]))

    while len(que) > 0:
        count = 1
        temp = que.popleft()

        while len(que) > 0 and temp >= que[0]:
            que.popleft()
            count += 1

        answer.append(count)

    return answer

print(solution([93,30,55], [1,30,5]))
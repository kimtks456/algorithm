from collections import deque


def solution(arr):
    answer = []
    deq = deque()
    deq.append(arr[0])

    for item in arr[1:]:
        if deq[-1] == item:
            continue
        deq.append(item)

    answer = list(deq)
    return answer
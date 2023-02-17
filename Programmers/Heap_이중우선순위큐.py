from heapq import heappush, heappop


def solution(operations):
    answer = []
    max_heap = []
    min_heap = []
    record = {}

    for cmd in operations:
        op, value = cmd[0], int(cmd[1:].strip())

        if op == 'I':
            heappush(max_heap, (-value, value))
            heappush(min_heap, value)
            if value in record.keys():
                record[value] += 1
            else:
                record[value] = 1

        elif value == 1:
            while True:
                if len(max_heap):
                    temp = heappop(max_heap)[1]
                    if record[temp]:
                        record[temp] -= 1
                        break
                else:
                    break
            continue

        else:
            while True:
                if len(min_heap):
                    temp = heappop(min_heap)
                    if record[temp]:
                        record[temp] -= 1
                        break
                else:
                    break

    small, large = 0, 0

    while True:
        if len(max_heap):
            large = heappop(max_heap)[1]
            if record[large] == 0:
                large = 0
            else:
                break
        else:
            break
    while True:
        if len(min_heap):
            small = heappop(min_heap)
            if record[small] == 0:
                small = 0
            else:
                break
        else:
            break

    answer += [large, small]
    return answer
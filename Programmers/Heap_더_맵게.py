from heapq import heapify, heappop, heappush


def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while scoville[0] < K and len(scoville) >= 2:
        answer += 1

        first = heappop(scoville)
        second = heappop(scoville)
        heappush(scoville, (first + 2 * second))

    if scoville[0] < K:
        answer = -1

    return answer


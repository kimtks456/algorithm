from collections import deque


def findNext(now, words):
    target = []
    for word in words:
        if sum(i == j for i, j in zip(now, word)) == len(now) - 1:
            target.append(word)
    return target


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    visited = set()
    visited.add(begin)

    while q:
        now, trial = q.popleft()

        if now == target:
            return trial

        cand = findNext(now, words)
        for word in cand:
            if word not in visited:
                q.append((word, trial + 1))
                visited.add(word)

    return answer
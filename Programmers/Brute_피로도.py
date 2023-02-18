from itertools import permutations as pm


def solution(k, dungeons):
    answer = -1
    cases = list(pm(dungeons, len(dungeons)))

    for case in cases:
        count = 0
        now = k
        for need, consume in case:
            if now >= need:
                count += 1
                now -= consume
        if answer < count:
            answer = count

    return answer
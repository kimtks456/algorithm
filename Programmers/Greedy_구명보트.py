def solution(people, limit):
    answer = 0
    people.sort()

    l, r = 0, len(people) - 1

    while l <= r:
        if people[l] + people[r] > limit:
            r -= 1
        else:
            l += 1
            r -= 1
        answer += 1

    return answer
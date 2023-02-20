from itertools import permutations as pm

# remove는 항상 조심 !!!! runtime error 뜰 수 있음.
def solution(name):
    answer = 0
    index = []

    # toggle
    tog = 0
    for idx, i in enumerate(name):
        if i != 'A':
            tog += min(ord(i) - ord('A'), 26 - ord(i) + ord('A'))
            index.append(idx)
    # move
    if 0 in index:
        index.remove(0)
    move = int(1e9)
    cases = pm(index, len(index))

    for case in cases:
        temp = 0
        prev = 0
        for i in case:
            temp += min(abs(i - prev), len(name) - abs(i - prev))
            prev = i
        move = min(move, temp)

    answer = tog + move

    return answer

# def solution(participant, completion):
#     answer = ''
#
#     for name in completion:
#         participant.remove(name)
#
#     if len(participant) == 0:
#         return answer
#
#     return participant[0]


# from collections import Counter
#
# def solution(participant, completion):
#     p = set(participant)
#     c = set(completion)
#
#     if len(p) > len(c):
#         return (p - c).pop()
#
#     count = Counter(participant)
#     dup = [(k, v) for k, v in count.items() if v > 1]
#
#     maxv = 0
#     answer = ''
#     for k, v in dup:
#         if maxv < v:
#             maxv = v
#             answer = k
#
#     return answer


from collections import Counter

def solution(participant, completion):
    p = set(participant)
    c = set(completion)

    if len(p) > len(c):
        return (p - c).pop()

    count_p = Counter(participant)
    dup_p = [(k, v) for k, v in count_p.items() if v > 1]
    count_c = Counter(completion)
    dup_c = [(k, v) for k, v in count_c.items() if v > 1]

    for item in dup_p:
        if item not in dup_c:
            return item[0]


def solution(participant, completion):
    # Counter끼리 뺄셈 속도 높이기 위해
    participant.sort()
    completion.sort()

    count_p = Counter(participant)
    count_c = Counter(completion)
    result = dict(count_p - count_c)

    return list(result.keys())[0]

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}

    for part in participant:
        # hash() return unique integer correspond to 'part'
        dic[hash(part)] = part
        temp += hash(part)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
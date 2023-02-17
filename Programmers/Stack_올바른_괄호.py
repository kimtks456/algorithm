from collections import deque


def solution(s):
    answer = True

    stack = deque(s[0])

    for item in s[1:]:
        if item == '(':
            stack.append(item)
            continue
        if len(stack) == 0:
            answer = False
            break
        stack.pop()

    if len(stack) > 0:
        answer = False

    return answer
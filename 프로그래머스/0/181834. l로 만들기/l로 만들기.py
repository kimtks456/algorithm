def solution(myString):
    answer = "".join(list(map(lambda x: 'l' if ord(x) - ord('l') < 0 else x, myString)))
    return answer
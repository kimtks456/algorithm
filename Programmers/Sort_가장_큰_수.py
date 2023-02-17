from functools import cmp_to_key


# def solution(numbers):
#     answer = ''

#     str_form = list(map(str, numbers))
#     str_form.sort(key = lambda x : x * 3, reverse = True)
#     answer = str(int(''.join(str_form)))
#     return answer

def str_compare(x, y):
    v1 = int(x + y)
    v2 = int(y + x)
    return (v1 > v2) - (v1 < v2)


def solution(numbers):
    str_form = list(map(str, numbers))
    str_form.sort(key=cmp_to_key(str_compare), reverse=True)
    return str(int(''.join(str_form)))
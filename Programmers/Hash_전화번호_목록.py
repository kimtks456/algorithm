# # 이렇게하니 맨 마지막 효율성 테스트 2개 시간초과 남. Hash를 이용하긴 해야함.
# def solution(phone_book):
#     answer = True
#     n = len(phone_book)
#
#     phone_book.sort(key=lambda x: len(x))
#
#     for i, num in enumerate(phone_book, start=1):
#         temp = list(map(lambda x: x[:len(num)], phone_book[i:]))
#         if num in temp:
#             return False
#     return answer

# Hash 안써도 통과 됨. sort할때, 길이별로가 아니라 사전순으로 해야 필요없는 비교 없음.
def solution(phone_book):
    answer = True

    # phone_book.sort(key = lambda x : len(x))
    phone_book.sort()

    for prev, now in zip(phone_book, phone_book[1:]):
        if len(prev) <= len(now) and now[:len(prev)] == prev:
            return False

    return answer

# Hash 풀이. list에 비해 약 1000배 넘게 빠를 수 있음. 길이 길어지면.
def solution(phone_book):
    answer = True

    numbers = set(phone_book)
    for i in range(len(phone_book)):
        temp = len(phone_book[i])
        for j in range(1, temp):
            if phone_book[i][:j] in numbers:
                return False
    return answer
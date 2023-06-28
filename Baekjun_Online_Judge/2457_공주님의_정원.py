import sys
from collections import deque
read = sys.stdin.readline

'''
반례 모음
https://www.acmicpc.net/board/view/86573

이렇게 작성하니 매번 정렬하므로 시간 초과.
(시작, 끝) 모두 오름차순으로 정렬 한번만 한 후, target_end를 땡기는 식으로 접근해야 정렬 안해도됨.
'''
def main():
    n = int(read())
    cases = []
    target_start, target_end = 301, 1130
    answer = 0
    for _ in range(n):
        cases.append(tuple(read().split()))
    cases = deque(conv2num(cases))

    while len(cases):
        cases = preprocess_and_sort(cases, target_start, target_end)
        # print(list(cases), target_start, target_end)
        # print(answer)
        start, end = cases.popleft()

        if start > target_start:
            print(0)
            return 0

        if target_start > target_end:
            break

        if start <= target_start < end:
            target_start = end
            answer += 1

    if target_start < target_end + 1:
        print(0)
        return 0

    print(answer)


# 공백 있는 날짜를 정수로 변환 ex) 1 1 5 31 -> 101 531
def conv2num(cases):
    for i, (m1, d1, m2, d2) in enumerate(cases):
        start, end = int(m1 + date_form(d1)), int(m2 + date_form(d2))
        cases[i] = (start, end)
    return cases


# start, end 날짜 넘어가면 target start, end에 맞춰 변환 및 정렬
def preprocess_and_sort(cases, target_start, target_end):
    for i, nums in enumerate(list(cases)):
        start, end = nums[0], nums[1]
        if start < target_start:
            start = target_start
        if end > target_end:
            end = target_end + 1
        cases[i] = (start, end)
    return deque(sorted(cases, key=lambda x: (x[0], -x[1])))

def date_form(num):
    if len(num) == 1:
        return '0' + num
    # 그냥 월에 100 곱하고 날짜 더해도 됨.
    return num


main()
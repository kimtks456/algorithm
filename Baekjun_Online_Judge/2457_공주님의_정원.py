import sys
read = sys.stdin.readline


'''
반례 모음
https://www.acmicpc.net/board/view/86573
답
https://wooono.tistory.com/607
'''


def main():
    n = int(read())
    cases = []
    target_start, target_end = 301, 301
    answer = 0
    for _ in range(n):
        cases.append(tuple(read().split()))
    cases = conv2num(cases)
    cases = preprocess_and_sort(cases, target_start, 1130)

    while len(cases):
        # print(cases, target_start, target_end)
        # print(answer)

        if target_end >= 1131 or cases[0][0] > target_end:
            break

        temp_target_end = -1

        for _ in range(len(cases)):
            if cases[0][0] <= target_end:
                if temp_target_end < cases[0][1]:
                    temp_target_end = cases[0][1]
                cases.remove(cases[0])
            else:
                break

        target_end = temp_target_end
        answer += 1

    if target_end <= 1130:
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
    for i, nums in enumerate(cases):
        start, end = nums[0], nums[1]
        if start < target_start:
            start = target_start
        if end > target_end:
            end = target_end + 1
        cases[i] = (start, end)
    return sorted(cases)

def date_form(num):
    if len(num) == 1:
        return '0' + num
    # 그냥 월에 100 곱하고 날짜 더해도 됨.
    return num


main()
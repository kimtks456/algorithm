def solution(N, number):
    answer = 0

    # 마지막 테스트 케이스 예외 : N = number
    if N == number:
        return 1

    use = [set() for i in range(8)]
    for i, s in enumerate(use):
        # 1 ~ 8 번 사용
        s.add(int(str(N) * (i + 1)))

    # 1 + 7 이 최대 횟수이니 7까지만 진행. 8번 쓰는건 이미 위에서 넣음.
    for i in range(1, 8):
        for j in range(i):
            for less in use[j]:
                # i가 되려면 1 + i-1이 최대
                for many in use[i - j - 1]:
                    use[i].add(less + many)
                    use[i].add(less * many)
                    use[i].add(less - many)
                    if many != 0:
                        use[i].add(less / many)
        if number in use[i]:
            answer = i + 1
            break
    else:
        answer = -1

    return answer
def solution(sequence, k):
    answer = []
    n = len(sequence)
    presum = [sequence[0]] * n
    for i in range(1, n):
        presum[i] = presum[i - 1] + sequence[i]

    print(presum)
    l, r = 0, n - 1
    while 0 <= l <= r < n:
        temp = presum[r] - presum[l] + sequence[l]

        if temp == k:
            if answer:
                ll, rr = answer[0], answer[1]
                if (rr - ll > r - l) or (rr - ll == r - l and ll > l):
                    answer[0], answer[1] = l, r
            else:
                answer.append(l)
                answer.append(r)
            l += 1
            r -= 1

        elif temp < k:
            l += 1
        else:
            r -= 1

    return answer
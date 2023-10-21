def solution(sequence, k):
    answer = []
    n = len(sequence)
    presum = [sequence[0]] * n
    for i in range(1, n):
        presum[i] = presum[i - 1] + sequence[i]

    for i in range(n):
        for j in range(i + 1):

            temp = presum[i] - presum[j] + sequence[j]
            if temp == k:
                if answer:
                    ll, rr = answer[0], answer[1]
                    if (rr - ll > i - j) or (rr - ll == i - j and ll > j):
                        answer = [j, i]
                else:
                    answer.append(j)
                    answer.append(i)

    return answer
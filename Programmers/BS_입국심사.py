def solution(n, times):
    answer = 0
    l, r = 1, max(times) * n

    while l <= r:
        mid = (l + r) // 2
        p = 0

        for t in times:
            p += (mid) // t
            if p >= n:
                break

        if p < n:
            l = mid + 1
        elif p >= n:
            answer = mid
            r = mid - 1

    return answer
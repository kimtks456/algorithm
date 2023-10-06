n = int(input())
k = int(input())

l, h = 1, k

while l <= h:
    count = 0

    # mid 보다 작거나 같은 숫자의 개수 = count
    mid = (l + h) // 2

    for i in range(1, n + 1):
        count += min(n, mid // i)

    if count >= k:
        """
        count와 k가 정확히 같지 않을 수 있음.
        ex) k = 7인데 mid = 6인게 8개, mid = 5인게 6개라면, k와 count는 절대 같을 수 없음.
        이 경우는 같은 mid가 여러개라 발생. k번째를 구하는 것이므로 count값이 더 커도 됨.
        같은 mid 값이 더 세아려지니까 count가 증가한 것이므로. 
        따라서 answer로 미리 기록해두고 BINS는 계속 돌려줌. 
        mid가 더 작아져서 count < k가 된다면 이전에 기록한 answer가 맞으니까.
        """
        # count와 k가 정확히 같지 않을 수 있음.
        answer = mid
        h = mid - 1
    else:
        l = mid + 1

print(answer)

"""
1~n
2~2*n

1 2 3 2 4 6 3 6 9
1 2 2 3 3 4 6 6 9

1  2  3  4  5
2  4  6  8 10
3  6  9 12 15
4  8 12 16 20
5 10 15 20 25
"""

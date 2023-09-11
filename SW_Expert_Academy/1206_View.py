T = 10
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0

    for col in range(2, n-2):
        for i in range(1, arr[col] + 1):
            if arr[col - 1] >= i or arr[col - 2] >= i or arr[col + 1] >= i or arr[col + 2] >= i:
                continue
            answer += 1

    print(f'#{test_case} {answer}')


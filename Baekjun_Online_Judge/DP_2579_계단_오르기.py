import sys
input = sys.stdin.readline


n = int(input())
stair = [int(input()) for _ in range(n)]

dp = [0] * n
if n < 3:
    print(sum(stair))
else:
    for i in range(2, n):
        dp[0], dp[1] = stair[0], stair[0] + stair[1]
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
    print(dp[n - 1])


'''
문제에서 필요한 조건 중 3번을 만족시키기 위해 맨 마지막 계단(= END)이 밟혀있다고 가정해보자.

그렇다면 그 전의 계단은 "END - 1" 계단이거나, 맨 마지막 "END - 2" 계단 일 것이다.

 

두 개의 경우에 문제 2번 조건을 적용시켜보자

밟은 계단이 "END - 1"일 경우 반드시 "END - 2" 계단을 밟으면 안 된다. - case_A

밟은 계단이 "END - 2"일 경우 그 전 계단은 신경 쓰지 않는다. - case_B

 

내가 만약 다이나믹 프로그래밍을 통해 배열 "dp"에 앞에서부터 밟아온 계단 중 가장 최대의 값을 저장해 왔다면 다음 수식처럼 정리할 수 있다. ex) dp[4] => 네 번째 계단까지 계산했을 때 가장 큰 경우 값을 저장

dp[i] = max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1])

수식을 한국말로 해설해보면

"i번 째 계단까지의 최대 가중치 합" = "case_B : i - 2번째 계단까지의 최대 가중치 합 + 현재 계단의 가중 치"와 "case_A : i- 3번째 계단까지의 최대 가중치 합 + i - 1번째 계단의 가중치 + 현재 계단의 가중 치" 중 더 큰 값

수식을 이렇게 정리해 보니 어떤 값이 선택되든 현재 계단의 가중 치가 포함되어있기 때문에 3번 조건을 만족하게 되면서 풀이 완성되었다.


https://sungmin-joo.tistory.com/18
'''

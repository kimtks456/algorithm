def levenshtein_distance(a: str, b: str) -> int:
    n, m = len(a), len(b)

    # DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 초기값 세팅
    for i in range(n + 1):
        dp[i][0] = i  # b가 빈 문자열 -> 모두 삭제
    for j in range(m + 1):
        dp[0][j] = j  # a가 빈 문자열 -> 모두 삽입

    # 점화식 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,    # 삭제
                    dp[i][j - 1] + 1,    # 삽입
                    dp[i - 1][j - 1] + 1 # 교체
                )
    return dp[n][m]

# 실행 예시
print(levenshtein_distance("kitten", "sitting"))  # 3

def solution(brown, yellow):
    answer = []
    n = brown + yellow
    dividor = [(i, n // i) for i in range(3, n // 2 + 1) if n % i == 0 and i <= n // i]
    
    for i, j in dividor:
        if (i - 2) * (j - 2) == yellow:
            answer = [j, i]
    
    return answer
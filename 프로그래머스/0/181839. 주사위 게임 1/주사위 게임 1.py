def solution(a, b):
    answer = 0
    
    if (a + b) % 2 == 1: 
        # 하나만 홀수
        answer = 2 * (a + b)
    else:
        if a % 2 == 1:
            # 둘 다 홀수
            answer = a ** 2 + b ** 2
        else:
            # 둘 다 짝수
            answer = abs(a - b)
            
    return answer
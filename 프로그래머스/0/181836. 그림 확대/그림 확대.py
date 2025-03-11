def solution(picture, k):
    answer = []
    
    for row in picture:
        temp = "".join([c * k for c in row])
        answer.extend([temp for i in range(k)])
        
    return answer
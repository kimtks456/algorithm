def solution(order):
    answer = 0
    
    for str in order:
        if 'cafelatte' in str:
            answer += 5000
        else:
            answer += 4500
            
    return answer
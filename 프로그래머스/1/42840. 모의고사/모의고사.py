def solution(answers):
    answer = []
    score = dict()
    
    # 1번 수포자
    idx, temp_score = 0, 0
    while idx < len(answers):
        if answers[idx] == (idx) % 5 + 1:
            temp_score += 1
        idx += 1
    score[1] = temp_score
    
    # 2번 수포자
    idx, temp_score, arr = 0, 0, [1, 3, 4, 5]
    while idx < len(answers):
        if idx % 2 == 0 and answers[idx] == 2:
            temp_score += 1
        elif idx % 2 == 1 and answers[idx] == arr[((idx - 1) // 2) % 4]:
            temp_score += 1
        idx += 1
    score[2] = temp_score
        
    # 3번 수포자
    idx, temp_score, arr = 0, 0, [3, 1, 2, 4, 5]
    while idx < len(answers):
       	if answers[idx] == arr[(idx // 2) % 5]:
            temp_score += 1
        idx += 1
    score[3] = temp_score
    
    max_score = max(score.values())
    
    for k, v in score.items():
        if v == max_score:
            answer.append(k)
    
    # 예외 조건
    if len(answer) > 0:
        answer.sort()
        
    return answer
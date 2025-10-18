from math import ceil

def solution(fees, records):
    answer = []
    parked = dict()
    total = dict()
    
    for record in records:
        time, num, inout = record.split(' ')
        
        if inout == 'IN':
            parked[num] = time
            if num not in total.keys():
                total[num] = 0
        else:
            in_time = parked[num]
            del parked[num]
            period = get_time_diff(in_time, time)
            total[num] += period
    
    # 잔여 주차된 차 정산
    for num, time in parked.items():
        period = get_time_diff(time, '23:59')
        total[num] += period
   	
    # 비용 계산
    for _, period in sorted(total.items(), key=lambda x: x[0]):
        cost = fees[1]
        if period > fees[0]:
            cost += ceil((period - fees[0]) / fees[2]) * fees[3]
        answer.append(cost)    
    return answer

def get_time_diff(start, end):
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))
    
    if em < sm:
        eh -= 1
        em += 60
    
    return (eh - sh) * 60 + em - sm
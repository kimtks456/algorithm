from collections import deque

def solution(bridge_length, weight, truck_weights):
    que = deque([0 for _ in range(bridge_length)])
    total_weight = sum(truck_weights)
    passed_weight, now_weight, answer = 0, 0, 0
    i = 0 # 현재 트럭 index
    
    while passed_weight < total_weight:
        temp = que.popleft()
        now_weight -= temp
        passed_weight += temp
        if i < len(truck_weights) and now_weight + truck_weights[i] <= weight:
            que.append(truck_weights[i])
            now_weight += truck_weights[i]
            i += 1
        else:
            que.append(0)
        answer += 1
    
    return answer
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliverySum, pickupSum = 0, 0
    
    for i in range(n-1, -1, -1):
        deliverySum += deliveries[i]
        pickupSum += pickups[i]
        cnt = 0
        
        while deliverySum > 0 or pickupSum > 0:
            deliverySum -= cap
            pickupSum -= cap
            cnt += 1
        
        answer += (i+1) * 2 * cnt
        
    return answer
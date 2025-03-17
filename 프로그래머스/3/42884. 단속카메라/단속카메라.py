def solution(routes):
    answer = 0
    n = len(routes)
    camera = -30000
    check = [False] * n
    
    # 진출 시점으로 정렬
    routes.sort(key=lambda x: x[1])
    print(routes)
    
    # 차량별 카메라 만났는지 check
    for i in range(n):
        s, e = routes[i]
        
        # 카메라 설치(처음엔 항상 설치해야함)
        if not check[i]:
            camera = e
            answer += 1
            
        # 이후 차량들에 대해 check 갱신
        for j in range(i+1, n):
            ss, ee = routes[j]
            if ss <= camera <= ee and not check[j]:
                check[j] = True
        
    return answer
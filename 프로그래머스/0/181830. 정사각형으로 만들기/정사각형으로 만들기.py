def solution(arr):
    y, x = len(arr), max([len(x) for x in arr])
    
    if y > x:
        for i in range(y):
            temp = y - len(arr[i])
            if temp > 0:
            	arr[i].extend([0] * (temp))
    elif y < x:
        for _ in range(x - y):
            arr.append([0] * x)
    
    return arr
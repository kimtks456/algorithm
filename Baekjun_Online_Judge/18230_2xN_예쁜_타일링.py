n, a, b = map(int, input().split())
weight1 = sorted(list(map(int, input().split())))
weight2 = sorted(list(map(int, input().split())))
answer = 0

if n % 2 != 0:
    n -= 1
    answer += weight1.pop()

while n:
    n -= 2
    if len(weight1) >= 2:
        w1, w2 = weight1.pop(), weight1.pop()
        if len(weight2) > 0:
            if w1 + w2 > weight2[-1]:
                answer += w1 + w2
            else:
                answer += weight2.pop()
                weight1.append(w2)
                weight1.append(w1)
        else:
            answer += w1 + w2
    else:
        answer += weight2.pop()

print(answer)
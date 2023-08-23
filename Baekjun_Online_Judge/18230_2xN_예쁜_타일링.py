n, a, b = map(int, input().split())
weight1 = list(map(int, input().split()))
weight2 = list(map(int, input().split()))
answer = 0

tile_b_count = n // 2
tile_a_count = n % 2
used_count = 0

while used_count <

weight1.sort()
while len(weight1) > 1:
    print(weight1)
    if n % 2 != 0 and len(weight1) == 2:
        break

    w1, w2 = weight1.pop(), weight1.pop()
    weight2.append(w1 + w2)

weight2.sort(reverse=True)
tile_b_count = n // 2

for i in range(tile_b_count):
    answer += weight2[i]
answer += 0 if n % 2 == 0 else weight1[-1]

print(answer)
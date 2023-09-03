import sys


n = int(input())
lines = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0
prev_s, prev_t = 0, 0

for i, line in enumerate(sorted(lines, key=lambda x: (x[0], x[1]))):
    if i == 0:
        prev_s, prev_t = line[0], line[1]
        if i == len(lines) - 1:
            answer += prev_t - prev_s
        continue

    s, t = line[0], line[1]
    if prev_t >= s:
        prev_t = max(t, prev_t)
        if i == len(lines) - 1:
            answer += prev_t - prev_s
    else:
        answer += prev_t - prev_s
        prev_s, prev_t = s, t
        if i == len(lines) - 1:
            answer += prev_t - prev_s

print(answer)




'''

6
-19 0
1 3
1 90
3 5
6 7
6 7
=108

1
1 2
=1

5
1 2
9 10
4 7
6 9
2 5
=9

4
5 10
15 20
25 30
7 35
= 30

'''
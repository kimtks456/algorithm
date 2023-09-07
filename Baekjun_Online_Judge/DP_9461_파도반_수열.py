import sys
input = sys.stdin.readline


p = [0] * 101
p[1], p[2], p[3], p[4], p[5] = 1, 1, 1, 2, 2
t = int(input())

for _ in range(t):
    n = int(input())
    for i in range(6, n + 1):
        p[i] = p[i - 1] + p[i - 5]
    print(p[n])



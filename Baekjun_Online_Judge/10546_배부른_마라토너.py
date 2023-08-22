import sys

n = int(input())
count = dict()
participants = [sys.stdin.readline().strip() for _ in range(n)]
complete = [sys.stdin.readline().strip() for _ in range(n - 1)]

for name in participants:
    if name not in count.keys():
        count[name] = 1
        continue
    count[name] += 1

for name in complete:
    count[name] -= 1

for name in count.keys():
    while count[name] > 0:
        print(name)
        count[name] -= 1
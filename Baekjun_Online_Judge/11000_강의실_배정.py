import sys
from heapq import heappop, heappush


n = int(input())
lectures = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
rooms = []
answer = 0

for s, t in sorted(lectures, key=lambda x: x[0] * 1e10 + x[1]):
    if not rooms:
        heappush(rooms, (t, (s, t)))
        answer += 1
        continue
    if rooms[0][0] > s:
        heappush(rooms, (t, (s, t)))
        answer += 1
    else:
        heappop(rooms)
        heappush(rooms, (t, (s, t)))
    # print(rooms)

print(answer)
'''

6
1 3
2 4
3 5
4 6
1 5
5 6
=3

8
1 8
9 16
3 7
8 10
10 14
5 6
6 11
11 12
=3

5
1 7
2 3
3 4
4 8
7 10
=2


'''
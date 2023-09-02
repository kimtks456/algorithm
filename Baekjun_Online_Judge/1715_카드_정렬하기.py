import sys
from heapq import heapify, heappop, heappush


n = int(input())
nums = [int(sys.stdin.readline()) for _ in range(n)]
heapify(nums)
answer = 0

while len(nums) >= 2:
    s1, s2 = heappop(nums), heappop(nums)
    answer += s1 + s2
    heappush(nums, s1 + s2)
print(answer)

'''

5
10 
30 
31
32
100

X
40 : 40 31 32 100
71 : 71 32 100
103 : 103 100
203
=> 417

[100, 40, 32, 31]
[100, 63, 40]
[103, 100]
[203]
=> 409
'''
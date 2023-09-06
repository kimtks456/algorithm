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
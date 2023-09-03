import sys
from heapq import heappop, heappush, heapify


n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
heapify(nums)

while m > 0:
    n1, n2 = heappop(nums), heappop(nums)
    heappush(nums, n1 + n2)
    heappush(nums, n1 + n2)
    m -= 1

print(sum(nums))
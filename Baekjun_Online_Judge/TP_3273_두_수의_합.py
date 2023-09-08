import sys
input = sys.stdin.readline


n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()

left, right = 0, n - 1
answer = 0

while 0 <= left < right <= n - 1:
    temp = nums[left] + nums[right]

    if temp == x:
        answer += 1
        left += 1
        right -= 1

    elif temp < x:
        left += 1
    else:
        right -= 1

print(answer)




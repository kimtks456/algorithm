n = int(input())
nums = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

nums.sort()
l, r = 0, len(nums) - 1

# for i in target:
#     while l <= r:
#         mid = (l + r) // 2
#         if nums[mid] < i:

for i in target:
    if i in nums:
        print(1)
    else:
        print(0)
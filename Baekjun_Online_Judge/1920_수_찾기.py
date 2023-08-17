n = int(input())
nums = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

nums.sort()
l, r = 0, len(nums) - 1

for i in target:
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == i:
            print(1)
            break
        elif nums[mid] < i:
            l = mid + 1
        else:
            r = mid - 1
    else:
        print(0)
    l, r = 0, len(nums) - 1

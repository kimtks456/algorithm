n = int(input())

def recursive(n):
    if n == 1 or n == 2:
        return 1
    return recursive(n-1) + recursive(n-2)

def dp(n):
    nums = [1, 1]
    answer = 0
    for i in range(3, n + 1):
        answer += 1
        nums.append(nums[i - 2] + nums[i - 3])
    return answer

print(recursive(n), dp(n))
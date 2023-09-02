import sys


n = int(input())
nums = [int(sys.stdin.readline()) for _ in range(n)]
answer = 0
nums.sort(reverse=True)

while len(nums) >= 2:
     # print(nums)
     s1, s2 = nums.pop(), nums.pop()
     temp = s1 + s2

     answer += temp

     i = len(nums) - 1
     while i >= 0:
          if nums[i] < temp:
               i -= 1
          else:
               break

     left = nums[:i+1]
     right = nums[i+1:]
     nums = left + [temp] + right
     print(nums)


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
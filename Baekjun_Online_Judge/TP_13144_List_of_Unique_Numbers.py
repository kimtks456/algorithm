import sys
input = sys.stdin.readline


N = int(input())
nums = list(map(int, input().split()))

l, r = 0, 0
count = 0
check = [False] * 100001

while r < N and l < N:
    if not check[nums[r]]:
        check[nums[r]] = True
        # 끝을 nums[r]로 하는 모든 수열 = r - l + 1
        count += r - l + 1
        r += 1
    else:
        # l을 옮김으로써 출발하는 수들 더이상 중복 아니게 False 처리
        check[nums[l]] = False
        l += 1

print(count)


"""
1 2 3 4 3

"""
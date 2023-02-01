import math
import sys
read = sys.stdin.readline

"""에라토스테네스의 체
장점 : O(N log(logN)) 으로 빠름.
단점 : 1~N까지 배열로 만들어야하기에 크기 N 배열 필요.
"""

"""Python의 메모리 제한. int형 기준
1,000 : 4KB
1,000,000 : 4MB

이 문제는 제한 128MB => 128,000,000 >= N
N이 100 이하이기에 가능.
"""

"""Python의 Set
- Hash Table로 구현돼 있기에 
x in set, remove 연산 O(1)으로 매우 빠름
"""


def main():
    while True:
        n = int(read())
        if n == 0:
            break

        nums = erathos(2 * n)
        print(sum(nums[n + 1:]))

def erathos(n):
    nums = [1 for i in range(n + 1)]
    nums[0], nums[1] = 0, 0

    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i] == 1:
            for j in range(2 * i, n+1, i):
                nums[j] = 0

    return nums

""" 아래처럼 Set이용해 하니 시간초과
def erathos(n):
    nums = set([i for i in range(2, n+1)])
    for i in range(2, int(math.sqrt(n)) + 1):
        j = 2
        while i * j <= n:
            nums.discard(i * j)
            j += 1
    return nums
"""
main()
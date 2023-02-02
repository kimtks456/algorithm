import sys
import math
read = sys.stdin.readline


def main():
    T = int(read())
    nums = []
    for _ in range(T):
        nums.append(int(read()))

    for num in nums:
        a, b = num//2, num//2
        while True:
            if is_prime(a) and is_prime(b):
                print(a, b)
                break
            a -= 1
            b += 1

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

main()
import sys
read = sys.stdin.readline


def main():
    n = int(read())
    nums = list(map(int, read().split()))

    nums_unique = sorted(list(set(nums)))
    order = dict()
    for i, num in enumerate(nums_unique):
        order[num] = i

    for i in nums:
        print(order[i], end=" ")

main()
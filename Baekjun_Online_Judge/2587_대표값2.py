import sys
read = sys.stdin.readline


def main():
    nums = []
    for _ in range(5):
        nums.append(int(read()))

    print(sum(nums) // 5)
    nums.sort()
    print(nums[2])


main()
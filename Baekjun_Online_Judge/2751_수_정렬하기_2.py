import sys
read = sys.stdin.readline


def main():
    n = int(read())
    nums = []
    for _ in range(n):
        nums.append(int(read()))
    nums.sort()

    for i in range(n):
        print(nums[i])


# def merge_sort(arr, l, r):
#     if l < r:
#         p = (l + r) // 2
#         merge_sort(arr, l, p)
#         merge_sort(arr, p+1, r)
#         merge(arr, l, p, r)

main()
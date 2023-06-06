import sys
read = sys.stdin.readline

# 메모리 초과. 다 받으면 안되고, 1~10000까지이니 개수를 저장.
def main():
    n = int(read())
    nums = [0] * 10001

    for i in range(n):
        temp = int(read())
        nums[temp] += 1

    for i in range(1, 10001):
        if nums[i] > 0:
            for j in range(nums[i]):
                print(i)

main()
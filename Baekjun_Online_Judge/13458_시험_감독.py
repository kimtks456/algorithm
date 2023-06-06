import sys
read = sys.stdin.readline


def main():
    N = int(read())
    nums = list(map(int, read().split()))
    B, C = map(int, read().split())

    result = 0
    for num in nums:
        result += 1
        if num-B <= 0:
            continue
        result += (num-B)//C + int((num-B)/C > (num-B)//C)
    print(result)

main()
import sys

def main():
    formular = sys.stdin.readline().rstrip()
    nums = formular.split('-')

    answer = sum(map(int, nums[0].split('+')))
    if len(nums) > 1:
        for i in range(1, len(nums)):
            answer -= sum(map(int, nums[i].split('+')))

    print(answer)

main()
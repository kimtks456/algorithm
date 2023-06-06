import sys
read = sys.stdin.readline
write = sys.stdout.write


def main():
    n = read().strip()
    nums = [n[i] for i in range(len(n))]
    nums.sort(reverse=True)
    # print(''.join(nums))
    write(''.join(nums))

main()

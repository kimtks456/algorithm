import sys
read = sys.stdin.readline


def main():
    n = int(read())
    fst_nums = set(map(int, read().split()))
    m = int(read())
    snd_nums = list(map(int, read().split()))

    for i in snd_nums:
        if i in fst_nums:
            print(1, end=' ')
        else:
            print(0, end=' ')



main()
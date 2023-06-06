import sys
read = sys.stdin.readline


def main():
    n = int(read())
    cnt = 0
    start = 666
    target = []
    while cnt < n:
        if is_contain_triple_six(start):
            target.append(start)
            cnt += 1
        start += 1
    print(target[-1])
    return 0

def is_contain_triple_six(n):
    seq = str(n)
    for i in range(len(seq)-2):
        if seq[i] == '6' and seq[i+1] == '6' and seq[i+2] == '6':
            return True
    return False


main()
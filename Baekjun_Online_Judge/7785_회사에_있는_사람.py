import sys
read = sys.stdin.readline


def main():
    n = int(read())
    remain = set()
    for _ in range(n):
        name, check = read().split()
        if check == 'enter':
            remain.add(name)
        else:
            remain.remove(name)

    remain = sorted(list(remain), reverse=True)
    for i in range(len(remain)):
        print(remain[i])



main()
import sys
read = sys.stdin.readline
from collections import Counter


def main():
    a = read().rstrip()
    a = a.lower()

    # 예외 처리
    if len(a) < 2:
        print(a.upper())
        return 0

    maxkey = Counter(a).most_common(2)
    if maxkey[0][1] == maxkey[1][1]:
        print('?')
        return 0
    print(maxkey[0][0].upper())
    return 0


main()
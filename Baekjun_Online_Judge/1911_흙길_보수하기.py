import sys
import math


def main():
    n, l = map(int, sys.stdin.readline().split())
    wells = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    wells.sort(key=lambda x: x[0])

    last_panel = 0
    answer = 0

    for i, j in wells:
        if i > last_panel:
            start = i
        else:
            start = last_panel + 1
        temp = math.ceil((j - start) / l)
        last_panel = start + temp * l - 1
        answer += temp

    print(answer)


main()

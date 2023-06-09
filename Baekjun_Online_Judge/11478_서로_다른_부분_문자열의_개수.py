import sys
from itertools import combinations
read = sys.stdin.readline


def main():
    seq = read().strip()
    unique = set()

    for item in seq:
        unique.add(item)

    index = [i for i in range(len(seq))]
    cases = list(combinations(index, 2))
    for idx1, idx2 in cases:
        unique.add(seq[idx1:idx2 + 1])

    print(len(unique))


main()
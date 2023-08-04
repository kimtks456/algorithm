import sys
from itertools import combinations


def calculate_score_diff(pair1, pair2):
    global answer
    first_score, second_score = 0, 0
    for i in range(len(pair1)):
        first_score += ability[pair1[i][0]][pair1[i][1]] + ability[pair1[i][1]][pair1[i][0]]
        second_score += ability[pair2[i][0]][pair2[i][1]] + ability[pair2[i][1]][pair2[i][0]]
    if abs(first_score - second_score) < answer:
        answer = abs(first_score - second_score)


n = int(input())
ability = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cases = list(combinations([i for i in range(n)], n//2))
answer = 20 * 20 * 100

for case in cases:
    first_pairs = list(combinations(case, 2))
    other_nums = [i for i in range(n) if i not in case]
    second_pairs = list(combinations(other_nums, 2))
    calculate_score_diff(first_pairs, second_pairs)

print(answer)
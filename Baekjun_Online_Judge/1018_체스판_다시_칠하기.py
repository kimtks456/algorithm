import sys
read = sys.stdin.readline


def main():
    # 입력
    n, m = map(int, read().split())
    maps = []
    for _ in range(n):
        maps.append(read().rstrip())

    # 8x8 window별로 최소 색칠칸 개수 세기
    min_cnt = 64
    for i in range(n - 8 + 1):
        for j in range(m - 8 + 1):
            temp_map = []
            for row in range(8):
                temp_map.append(maps[i + row][j:j + 8])
            cnt = find_minimum_coloring(temp_map)
            if min_cnt > cnt:
                min_cnt = cnt
    print(min_cnt)
    return 0

def find_minimum_coloring(maps):
    min_cnt1 = 64
    min_cnt2 = 64
    cnt = 0

    for idx, row in enumerate(maps):
        cnt += count_different_space(idx, row, 'BWBWBWBW', 'WBWBWBWB')
    if cnt < min_cnt1:
        min_cnt1 = cnt

    cnt = 0
    for idx, row in enumerate(maps):
        cnt += count_different_space(idx, row, 'WBWBWBWB', 'BWBWBWBW')
    if cnt < min_cnt2:
        min_cnt2 = cnt

    return min(min_cnt1, min_cnt2)

def count_different_space(idx, row, first, second):
    cnt = 0
    if idx % 2 == 0:
        for i in range(8):
            if row[i] != first[i]:
                cnt += 1
    else:
        for i in range(8):
            if row[i] != second[i]:
                cnt += 1
    return cnt

main()
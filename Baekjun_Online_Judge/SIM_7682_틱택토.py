import sys
read = sys.stdin.readline


while True:
    temp = read().rstrip()
    if temp == 'end':
        break

    # pre-process
    count_OX, count_lines = dict(), []
    count_OX['O'], count_OX['X'], count_OX['.'] = 0, 0, 0
    arr = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(9):
        arr[i // 3][i % 3] = temp[i]
        count_OX[temp[i]] += 1

    # 0. count(O) > count(X) 이면 불가
    if count_OX['O'] > count_OX['X'] or count_OX['O'] + 1 < count_OX['X']:
        print('invalid')
        continue

    # 1. 가로 or 세로 or 대각선 한 줄이 몇개인지 확인
    for i in range(3):
        # 가로
        if arr[i][0] == arr[i][1] == arr[i][2] != '.':
            count_lines.append(arr[i][0])
        # 세로
        if arr[0][i] == arr[1][i] == arr[2][i] != '.':
            count_lines.append(arr[0][i])

    # 대각선
    if (arr[0][0] == arr[1][1] == arr[2][2]) and arr[0][0] != '.':
        count_lines.append(arr[1][1])
    if (arr[2][0] == arr[1][1] == arr[0][2]) and arr[0][2] != '.':
        count_lines.append(arr[1][1])

    # for row in arr:
    #    print(row)
    # print(count_OX)
    # print(count_lines)
    # print()

    # 2. 0개 : '.'이 남아 있으면 안됨.
    if len(count_lines) == 0 and count_OX['.'] > 0:
        print('invalid')
        continue

    # 3. 1개
    if len(count_lines) == 1:
        # count(0) == count(X) : 줄은 O여야 함
        if count_OX['O'] == count_OX['X'] and count_lines[0] == 'X':
            print('invalid')
            continue
        # count(0) + 1 == count(X) : 줄은 X여야 함
        if count_OX['O'] + 1 == count_OX['X'] and count_lines[0] == 'O':
            print('invalid')
            continue

    # 4. 2개 : 'O'로 2개이면 불가
    if len(count_lines) == 2:
        if 'O' in count_lines:
            print('invalid')
            continue

    # 5. 3개 이상 : 불가
    if len(count_lines) > 2:
        print('invalid')
        continue

    print('valid')


"""
xo.
ox.
..x


oox
oxx
x..

xx.
oo.
x..

oxo
xox
oxx

oxo
xox
xoo
end

OXOXOXXOO
end

XO.XO.XO.
end
"""
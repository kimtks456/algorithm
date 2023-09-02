import sys

r, c = map(int, input().split())
strings = [list(sys.stdin.readline().strip()) for _ in range(r)]
count = r - 1
flag = True

while flag and count >= 0:
    if count == 0:
        print(count)
        break

    # 밑에서부터 String 만들기
    string_from_bottom = strings[count:]
    candidate = []

    for i in range(c):
        temp = ''
        for j in range(len(string_from_bottom)):
            temp += string_from_bottom[j][i]

        # 중복 검사
        if temp not in candidate:
            candidate.append(temp)
        else:
            count -= 1
            break
    else:
        print(count)
        break

import sys


n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]
answer = 0

char_count = dict()
for i in range(26):
    char_count[chr(ord('A') + i)] = 0

for string in strings:
    for i, character in enumerate(string):
        char_count[character] += 10 ** (len(string) - i - 1)

assign = dict()

count_result = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
num = 9
for character, weight in count_result:
    assign[character] = num
    num -= 1

for string in strings:
    temp = 0
    for i, character in enumerate(string):
        temp += assign[character] * 10 ** (len(string) - i - 1)
    answer += temp

print(answer)

'''


6
ACDEB
BCDEB
CABD
BDEFE
DDDDD
DABCD


'''
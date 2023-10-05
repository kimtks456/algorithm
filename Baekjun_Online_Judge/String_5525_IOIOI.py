n = int(input())
m = int(input())
s = input().rstrip()

pn = "IO" * n + "I"

i, answer = 0, 0
temp_count = 0

while i < m:
    if temp_count == n:
        answer += 1
        temp_count -= 1
    if i < m - 2 and ''.join([s[i], s[i + 1], s[i + 2]]) == "IOI":
        temp_count += 1
        i += 2
        continue
    else:
        i += 1
        temp_count = 0

print(answer)

# # BRTF 풀이법 -> 부분점수만 받음
# answer = 0
# for i in range(m - len(pn) + 1):
#     flag = True
#     for j in range(len(pn)):
#         flag = flag and (pn[j] == s[i + j])
#     if flag:
#         answer += 1
#
# print(answer)


# # dictionary 풀이법 -> 시간초과
# count = dict()
# for i in range(m - len(pn) + 1):
#     now = ""
#     for j in range(len(pn)):
#         now += s[i + j]
#     if now in count.keys():
#         count[now] += 1
#     else:
#         count[now] = 1
#
# print(count[pn])



"""

4
13
OOIOIOIOIIOII

"""
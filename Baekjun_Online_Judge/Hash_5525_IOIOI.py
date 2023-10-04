n = int(input())
m = int(input())
s = input().rstrip()

pn = ""
while len(pn) < 2 * n:
    pn += "IO"
pn += "I"

# # dictionary 풀이법
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

# BRTF 풀이법
answer = 0
for i in range(m - len(pn) + 1):
    flag = True
    for j in range(len(pn)):
        flag = flag and (pn[j] == s[i + j])
    if flag:
        answer += 1

print(answer)

"""

4
13
OOIOIOIOIIOII

"""
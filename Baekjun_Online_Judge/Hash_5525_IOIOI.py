n = int(input())
m = int(input())
s = input().rstrip()

pn = ""
while len(pn) < 2 * n:
    pn += "IO"
pn += "I"

count = dict()
for i in range(m - len(pn) + 1):
    now = ""
    for j in range(len(pn)):
        now += s[i + j]
    if now in count.keys():
        count[now] += 1
    else:
        count[now] = 1

print(count[pn])


"""

4
13
OOIOIOIOIIOII

"""
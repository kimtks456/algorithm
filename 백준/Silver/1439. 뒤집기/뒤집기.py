s = input().rstrip()

count = dict()
count['0'], count['1'] = 0, 0
prev = s[0]
count[prev] += 1

for ch in s[1:]:
    if prev == ch:
        continue
    count[ch] += 1
    prev = ch

print(min(count.values()))
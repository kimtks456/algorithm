import sys


n, k = map(int, sys.stdin.readline().split())
schedule = list(map(int, sys.stdin.readline().split()))
plug = []
answer = 0

# counter = dict()
# for name in schedule:
#     if name not in counter.keys():
#         counter[name] = 1
#     else:
#         counter[name] += 1
# print(counter)
# print()

# 사용 빈도 count 할 필요 없음
first_idx_of_plugs = []
for i in range(len(schedule)):
    # print(schedule[i:])
    # print(plug, answer, first_idx_of_plugs)
    # print()
    if schedule[i] in plug:
        continue

    if len(plug) < n:
        plug.append(schedule[i])

    # plug에 있는 기기 중, 가장 나중에 사용되는 기기 선택
    else:
        # 1. plug에 있는 기기들의 앞으로 사용될 첫번째 index 저장
        first_idx_of_plugs = dict()
        for name in plug:
            for idx in range(i+1, k):
                if name == schedule[idx]:
                    first_idx_of_plugs[name] = idx
                    break
            else:
                first_idx_of_plugs[name] = len(schedule)

        # 1-1. 앞으로 사용되지 않는다면, 아무 plug(맨뒤) 교체
        if len(first_idx_of_plugs) == 0:
            plug.pop()
            plug.append(schedule[i])
            answer += 1
            continue

        # 2. 가장 나중에 나오는 기기 선택
        max_idx, max_idx_name = 0, ''
        for name, idx in first_idx_of_plugs.items():
            if idx > max_idx:
                max_idx = idx
                max_idx_name = name

        # 3. 해당 기기 교체
        plug.pop(plug.index(max_idx_name))
        plug.append(schedule[i])
        answer += 1

print(answer)



        # # plug에 있는 기기 중, 앞으로 사용 횟수 가장 적은 기기 선택
        # min_count = 101
        # for name in plug:
        #     if min_count > counter[name]:
        #         min_count = counter[name]
        # for name in plug:
        #     if counter[name] == min_count:
        #         replace_candidate.append(name)

        # # 교체 후보가 1개일 시, 바로 교체
        # if len(replace_candidate) == 1:
        #     plug.pop(plug.index(replace_candidate[0]))
        #     plug.append(schedule[i])
        #     counter[schedule[i]] -= 1
        #     answer += 1
        #     print("replace : ", replace_candidate[0])
        #
        # # 교체 후보가 여러개일 시, 더 뒤에 사용될 기기 선택
        # else:
        #     first_idx_of_replace_candidate = dict()
        #     # 현재 이후로 처음 사용되는 순서 선택
        #     for candidate in replace_candidate:
        #         # schedule[i+1:] 에서 처음 사용되는 index 찾기
        #         for idx in range(i+1, len(schedule)):
        #             if schedule[idx] == candidate:
        #                 first_idx_of_replace_candidate[candidate] = idx
        #                 break
        #     print(first_idx_of_replace_candidate)
        #
        #     last_used_idx = max(first_idx_of_replace_candidate.values())
        #     # 가장 마지막 사용되는 기기 선택
        #     for name, first_idx in first_idx_of_replace_candidate.items():
        #         if first_idx == last_used_idx:
        #             target = name
        #
        #     plug.pop(plug.index(target))
        #     plug.append(schedule[i])
        #     counter[schedule[i]] -= 1
        #     answer += 1
        #     print("replace : ", target)

# print(answer)


'''

2 8
2 3 2 1 2 1 1 3
=2

3 100
56 71 70 25 52 77 76 8 68 71 51 65 13 23 7 16 19 54 95 18 86 74 29 76 61 93 44 96 32 72 64 19 50 49 22 14 7 64 24 83 6 3 2 76 99 7 76 100 60 60 6 50 90 49 27 51 37 61 16 84 89 51 73 28 90 77 73 39 78 96 78 13 92 54 70 69 62 78 7 75 30 67 97 98 19 86 90 90 2 39 41 58 57 84 19 8 52 39 26 7
=80

{56: 1, 71: 2, 70: 2, 25: 1, 52: 2, 77: 2, 76: 4, 8: 2, 68: 1, 51: 3, 65: 1, 13: 2, 23: 1, 7: 5, 16: 2, 19: 4, 54: 2, 95: 1, 18: 1, 86: 2, 74: 1, 29: 1, 61: 2, 93: 1, 44: 1, 96: 2, 32: 1, 72: 1, 64: 2, 50: 2, 49: 2, 22: 1, 14: 1, 24: 1, 83: 1, 6: 2, 3: 1, 2: 2, 99: 1, 100: 1, 60: 2, 90: 4, 27: 1, 37: 1, 84: 2, 89: 1, 73: 2, 28: 1, 39: 3, 78: 3, 92: 1, 69: 1, 62: 1, 75: 1, 30: 1, 67: 1, 97: 1, 98: 1, 41: 1, 58: 1, 57: 1, 26: 1}


'''

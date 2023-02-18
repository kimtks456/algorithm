def solution(n, lost, reserve):
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)

    _lost = sorted(list(_lost))
    _reserve= sorted(list(_reserve))

    answer = n - len(_lost)

    for i in _lost:
        prev, after = i - 1, i + 1
        if prev in _reserve:
            _reserve.remove(prev)
            answer += 1
        elif after in _reserve:
            _reserve.remove(after)
            answer += 1

    return answer

solution(4, [-1, 3, 1], [2, 4])
# def solution(n, lost, reserve):
#     answer = n - len(lost)
#
#     lost.sort()
#     reserve.sort()
#
#     new_lost = [l for l in lost if l not in reserve]
#     answer += len(lost) - len(new_lost)
#
#     for i in new_lost:
#         prev, after = i - 1, i + 1
# 이러면 reserve에서 안지워서 틀림
#         if prev in reserve:
#             reserve.remove(prev)
#             answer += 1
#
#         elif after in reserve:
#             reserve.remove(after)
#             answer += 1
#
#     return answer
#
# # def solution(n, lost, reserve):
# #     answer = n - len(lost)
# #
# #     # 정렬돼있다는 말이 없음! 잘봐!!
# #     lost.sort()
# #     reserve.sort()
# #
# #     # 이렇게하면 여벌있는데 도난당해서 원래 빌려주면 안되나,
# #     # prev in reserve로 인해 빌려주게될 수 있음
# #     for i in lost:
# #         prev, after = i - 1, i + 1
# #
# #         if i in reserve:
# #             reserve.remove(i)
# #             answer += 1
# #
# #         elif prev in reserve:
# #             reserve.remove(prev)
# #             answer += 1
# #
# #         elif after in reserve:
# #             reserve.remove(after)
# #             answer += 1
# #
# #     return answer
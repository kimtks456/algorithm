def solution(players, callings):
    name_idx = dict()
    idx_name = dict()

    for i, name in enumerate(players):
        name_idx[name] = i
        idx_name[i] = name

    for name in callings:
        now_idx = name_idx[name]
        prev_name = idx_name[name_idx[name] - 1]

        name_idx[name], name_idx[prev_name] = name_idx[prev_name], name_idx[name]
        idx_name[now_idx], idx_name[now_idx - 1] = idx_name[now_idx - 1], idx_name[now_idx]

    answer = ['a'] * len(players)
    for name, idx in name_idx.items():
        answer[idx] = name

    return answer
def dfs(start, visited, com):
    visited[start] = 1
    for i, neighbor in enumerate(com[start]):
        if i != start and visited[i] == 0 and neighbor == 1:
            dfs(i, visited, com)

    return visited


def solution(n, computers):
    answer = 1
    visited = [0] * n
    start = 0

    while True:
        visited = dfs(start, visited, computers)
        if False in visited:
            start = visited.index(False)
            answer += 1
        else:
            break
    return answer
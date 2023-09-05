m = 3
data = [1, 2, 3, 4]


def combination(arr, r):
    result = []

    def dfs(case, depth):
        if len(case) == r:
            result.append(case[:])
            return
        elif depth == len(arr):
            return

        case.append(arr[depth])
        dfs(case, depth + 1)

        case.pop()
        dfs(case, depth + 1)

    dfs([], 0)

    return result


def permutation(arr, r):
    result = []
    visited = [False] * len(arr)

    def dfs(case):
        if len(case) == r:
            result.append(case[:])
            return

        for i, v in enumerate(arr):
            if visited[i]:
                continue

            case.append(v)
            visited[i] = True
            dfs(case)

            case.pop()
            visited[i] = False

    dfs([])

    return result


print(combination(data, m))
print(permutation(data, m))

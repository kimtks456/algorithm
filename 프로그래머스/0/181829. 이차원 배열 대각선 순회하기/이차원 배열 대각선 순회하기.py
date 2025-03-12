def solution(board, k):
    answer = 0
    for i in range(k + 1):
        for j in range(k + 1):
            if i + j <= k and i < len(board) and j < len(board[i]):
                answer += board[i][j]
    return answer
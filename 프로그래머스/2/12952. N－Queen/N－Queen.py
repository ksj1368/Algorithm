def dfs(row, n, board):
    cnt = 0
    if n == row:  # 모든 퀸을 배치했을 경우 종료
        return 1
    for col in range(n):
        board[row] = col  # 현재 행(row)의 열(col)에 퀸 배치
        for i in range(row):
            # 같은 열에 위치하거나 대각선에 위치한 경우
            if board[i] == board[row] or abs(board[i] - board[row]) == row - i:
                break
        else:  # 모든 퀸이 한 번에 공격할 수 없을 경우 count + 1
            cnt += dfs(row + 1, n, board)
    return cnt

def solution(n):
    return dfs(0, n, [0] * n)
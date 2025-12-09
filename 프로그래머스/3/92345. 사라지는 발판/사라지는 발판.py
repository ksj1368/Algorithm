def solution(board, aloc, bloc):
    
    dx = [1,-1, 0, 0]
    dy = [0, 0, 1, -1]
    r, c = len(board), len(board[0])
    def dfs(cur, op):
        y, x = cur
        if board[y][x] == 0:
            return False, 0
        
        can_move = False
        wins = []
        loses = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and board[ny][nx] != 0:
                can_move = True
                board[y][x] = 0
                is_op_win, move_count = dfs(op, [ny, nx])
                board[y][x] = 1
                
                if is_op_win:
                    loses.append(move_count)
                else:
                    wins.append(move_count)
        if not can_move:
            return False, 0
        
        if wins:
            return True, min(wins) + 1
        else:
            return False, max(loses) + 1
                    
    _, total_moves = dfs(aloc, bloc)
    return total_moves

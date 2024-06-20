from collections import deque

def bfs(x, y, arr):
    q = deque([(x, y)])
    total = int(arr[x][y])
    arr[x][y] = 'X'
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] != "X":
                total += int(arr[nx][ny])
                arr[nx][ny] = "X"
                q.append((nx, ny))
                
    return total
        
def solution(maps):
    answer = []
    arr = [list(row) for row in maps]
        
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != "X":
                answer.append(bfs(i, j, arr))
    if not answer:
        return [-1]
    else:
        return sorted(answer)
#dfs
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    n = len(maps[0])
    m = len(maps)   
    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and ny >= 0 and ny < n and nx < m: 
                if maps[nx][ny] == 1:
                    q.append([nx,ny])
                    maps[nx][ny] += maps[x][y]
                if nx == m-1 and ny == n-1:
                    return maps[m-1][n-1]
    return -1
            
            
    
                
                
            
                
            
                

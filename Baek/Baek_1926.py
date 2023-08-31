"""
    @ Baek 1926, 그림
    @ Prob. https://www.acmicpc.net/problem/1926
      Ref. 
      Ref Prob.
    @ Algo: bfs
    @ Start day: 22. 11. 21
    @ End day: 22. 11. 21
"""
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
max_size = 0
q = deque()

arr = [list(map(int, input().split())) for _ in range(n)]
    
def dfs(x, y):
    arr[x][y] = 0
    q.append([x,y])
    size = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if ny >= 0 and nx >= 0 and ny < m and nx < n:
                if arr[nx][ny] == 1:
                    q.append([nx, ny])
                    arr[nx][ny] = 0
                    size +=1    
    return size

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            max_size = max(dfs(i,j), max_size)
            cnt +=1
            
print(cnt)
print(max_size)
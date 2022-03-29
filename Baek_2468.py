"""
    @ Baek 2468, 안전 영역
    @ Prob. https://www.acmicpc.net/problem/2468
      Ref. 
      Ref Prob. 
    @ Algo: BFS
    @ Start day: 22. 03. 29
    @ End day: 22. 03. 29
    문제를 이해하고 어떤 방식으로 풀어나갈지는 쉽게 생각했지만 구현하는 것은 어려웠음
    메인 함수의 2중 for문의 if문에서 물의 높이 보다 커야 BFS()를 실행하도록 구현했을 때 틀렸었다.
    물의 높이가 같은 경우에도 BFS()를 실행하도록 구현했을 때 맞았다.
    문제를 대충 읽어서 물의 높이와 지역의 높이가 같을 경우 침수했다고 생각했다.
    다음부터는 꼼꼼하게 문제를 읽어야겠다.
"""
import sys
input = sys.stdin.readline
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 너비 우선 탐색
def BFS(i, j, h):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1 # 방문 처리

    while q:
        x, y = q.popleft()

        for k in range(4): # 탐색 영역
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0<= nx <N and 0<= ny <N:                        # 2차원 배열의 범위 내에서
               if arr[nx][ny] >= h and visited[nx][ny] != 1:   # 침수가 안되어있고 방문하지 않을 경우
                    q.append([nx, ny])
                    visited[nx][ny] = 1                        # 방문 처리

N = int(input()) # 행, 열 입력(N*N)
arr = []
safety_area = 0
arr = [list(map(int, input().split())) for _ in range(N)] # 배열 입력

mn = min(map(min, arr)) # 최소 높이
mx = max(map(max, arr)) # 최대 높이

for h in range(mn, mx+1): # 최대 높이까지 물이 찰때 동안
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):    
        for j in range(N):
            if arr[i][j] >= h and visited[i][j] == 0: # 땅의 높이가 물과 같거나 더 높고 방문을 안헀을 경우
                BFS(i, j, h)
                cnt +=1
                
    if cnt > safety_area: # 안전한 땅이 더 많을 경우 
        safety_area = cnt # 할당  

print(safety_area)
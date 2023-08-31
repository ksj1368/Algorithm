"""
    @ Baek 11724, 연결 요소의 개수
    @ Prob. https://www.acmicpc.net/problem/11724
      Ref. 
      Ref Prob. 
    @ Algo: BFS
    @ Start day: 22. 03. 28
    @ End day: 22. 03. 28
    bfs를 사용하여 경로 탐색, 처음 선택한 정점과 이어져있지 않을 경우 다시 bfs 실행
"""
import sys
input = sys.stdin.readline

def BFS(i):
    q = [i]
    while q:
        i = q.pop(0)
        for j in arr[i]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = 1 # 방문처리
                
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1, N+1):
    if visited[i] == 0:
        BFS(i)
        cnt +=1
print(cnt)

"""
시간 초과 코드
import sys
from collections import deque
input = sys.stdin.readline
def BFS(i, j):
    q = deque()
    q.append([i, j])
    arr[i][j] = 0
    
    while q:
        x, y = q.popleft()
        for k in range(N):
            if arr[y][k] == 1:
                q.append([y, k])
                arr[y][k] = 0
                
N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    arr[u][v] = 1
    arr[v][u] = 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            BFS(i, j)
            cnt +=1
print(cnt)
"""
"""
    @ Baek 4963, 섬의 개수
    @ Prob. https://www.acmicpc.net/problem/4963
      Ref. 
      Ref Prob. 
    @ Algo: BFS
    @ Start day: 22. 03. 26
    @ End day: 22. 03. 26
"""
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def BFS(x, y):
    global cnt
    q = deque()
    q. append([x, y])
    arr[x][y] = 0
    while q:
        qx, qy = q.popleft()
        for i in range(8):
            nx = dx[i] + qx
            ny = dy[i] + qy
            if 0 <= nx < h and 0 <= ny <w and arr[nx][ny] == 1:
                q.append([nx, ny])
                arr[nx][ny] = 0
    cnt += 1
    

while True:
    arr = []
    cnt = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        for _ in range(h):
            arr.append(list(map(int, input().split())))
    for x in range(h):
        for y in range(w):
          if arr[x][y] == 1:
            BFS(x, y)
            
    print(cnt)

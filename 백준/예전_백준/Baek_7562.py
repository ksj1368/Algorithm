"""
    @ Baek 7562, 나이트의 이동
    @ Prob. https://www.acmicpc.net/problem/7562
      Ref. 
      Ref Prob. 
    @ Algo: DFS, BFS
    @ Start day: 22. 03. 23
    @ End day: 22. 03. 23
"""
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def BFS(x, y, arrival_x, arrival_y):
    q = deque()
    q.append([x, y])
    chs[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == arrival_x and y == arrival_y:
            return chs[arrival_x][arrival_y]-1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < M and chs[nx][ny] == 0:
                q.append([nx, ny])
                chs[nx][ny] = chs[x][y] + 1

test_case = int(input())
for _ in range(test_case):
    M = int(input())
    x, y = map(int, input().split())
    arrival_x, arrival_y = map(int, input().split())
    chs = [[0]*M for _ in range(M)]
    print(BFS(x, y, arrival_x, arrival_y))
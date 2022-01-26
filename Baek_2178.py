"""
    @ Baek 2178, 미로탐색
    @ Prob. https://www.acmicpc.net/problem/2178
      Ref.
      Ref Prob. 
    @ Algo: bfs
    @ Start day: 22. 01. 22
    @ End day: 22. 01. 22
    bfs를 이용해 주변에 "1"이 있는 인덱스를 탐색한다. "1"인 인덱스를 탐색하면 인덱스에 1을 더해주고 이를 반복한다.
    마지막 인덱스에 도착을 하면 탐색을 종료하고 누적된 값을 출력한다.
"""

import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    global ans
    q = [[x, y]]
    graph[x][y] = 0

    while q:
        x = q[0][0]
        y = q[0][1]
        del q[0]

        for i in range(4):
            x_new = x + dx[i]
            y_new = y + dy[i]

            if 0<=x_new<N and 0<=y_new<M:    # graph 크기에 x_new, y_new가 있으며       
                if graph[x_new][y_new] == 1: # 벽이 아닐 경우
                    graph[x_new][y_new] =  graph[x][y] + 1
                    q.append([x_new, y_new])
                    
    return graph[N-1][M-1] # 미로의 마지막 칸에 도착할 경우 종료

N, M = map(int, input().split()) # N = 세로, M = 가로
graph = []

for _ in range(N):
    graph.append(list(map(int, input().strip())))

print(bfs(0, 0)+1)
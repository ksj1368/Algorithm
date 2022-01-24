"""
    @ Baek 2667, 단지번호붙이기
    @ Prob. https://www.acmicpc.net/problem/2667
      Ref. 
      Ref Prob. 
    @ Algo: 
    @ Start day: 22. 01. 21
    @ End day: 22. 01. 21
"""
import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(j,i):
    q = [[j,i]]
    graph[j][i] = 0
    global cnt
    while q:
        x, y = q[0][0], q[0][1]
        del q[0]

        for k in range(4):
            x_new = x + dx[k]
            y_new = y + dy[k]
            if 0<= x_new <N and 0<= y_new <N:
                if graph[x_new][y_new] == 1:
                    
                    q.append([x_new, y_new])
                    graph[x_new][y_new] = 0
                    cnt +=1

N = int(input())
graph = []
ans = []
cnt = 1
                    
for _ in range(N):
    graph.append(list(map(int,input().strip())))

for i in range(N):
    for j in range(N):
        if graph[j][i] == 1:
            bfs(j, i)
            ans.append(cnt)
            cnt = 1

print(len(ans))

for idx in sorted(ans):
    print(idx)
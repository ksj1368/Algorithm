"""
    @ Baek 1012, 유기농 배추
    @ Prob. https://www.acmicpc.net/problem/1012
      Ref. 
      Ref Prob. 
    @ Algo: bfs
    @ Start day: 22. 01. 20
    @ End day: 22. 01. 20
    bfs나 dfs를 적용해서 풀이 가능
    bfs를 연습하기 위해 bfs로 풀이
    지렁이가 배추를 방문할 경우 배추(1)를 0으로 바꿔줌
"""
import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,-1, 1]


def bfs(c, r):
    q = [[c,r]]
    area[c][r] = 0

    while q:
        a, b = q[0][0], q[0][1]
        
        del q[0]
        for i in range(4):
            nc = a + dx[i]                  ## 현재 위치에서 상하좌우 탐색
            nr = b + dy[i]
            if 0 <= nc < n and 0 <= nr < m: # area 범위 내에
                if area[nc][nr] == 1:       # 1일 경우
                    area[nc][nr] = 0        # 방문
                    q.append([nc, nr])      # 큐에 방문 위치 추가
        
test_case = int(input())

for _ in range(test_case):
    m, n, cabbage = map(int, input().split()) # m = 가로, n = 세로
    area = [[0]*m for _ in range(n)]    
    ans = 0
    for _ in range(cabbage):
        x, y = map(int, input().split())
        area[y][x] = 1                        # 양배추 = 1
    for c in range(n):
        for r in range(m):
            if area[c][r] == 1:
                bfs(c, r)
                ans +=1
    print(ans)
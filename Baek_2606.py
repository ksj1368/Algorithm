"""
    @ Baek 2606, 바이러스
    @ Prob. https://www.acmicpc.net/problem/2606
      Ref.
      Ref Prob. 
    @ Algo: dfs
    @ Start day: 22. 01. 19
    @ End day: 22. 01. 19
   재귀함수를 이용한 깊이 우선 탐색으로 구현
   dfs를 사용해 간단하게 풀이
"""
import sys
input = sys.stdin.readline

def dfs(start):
    global answer
    visited[start] = 1
    for i in range(1, com+1):
        if visited[i] == 0 and graph[start][i] == 1:
            answer +=1
            dfs(i)

com = int(input())
graph = [[0] * (com + 1) for _ in range(com + 1)]
visited = [0]*(com+1)
line = int(input())
answer = 0

for _ in range(line): 
   x, y = map(int, input().split())
   graph[x][y] = 1 # 노드끼리 연결되어 있을 경우 1, 연결이 안되있을 경우 0
   graph[y][x] = 1

dfs(1)
print(answer)
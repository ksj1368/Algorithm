"""
    @ Baek 1260, DFS와 BFS
    @ Prob. https://www.acmicpc.net/problem/1260
      Ref.
      Ref Prob. https://pacific-ocean.tistory.com/260
    @ Algo: 재귀함수, Queue
    @ Start day: 22. 01. 13
    @ End day: 22. 01. 13  
    너비우선탐색은 큐로 구현, 깊이우선탐색(dfs)는 재귀함수로 구현
"""
import sys
import queue

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0]*(N+1)
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(V):
    print(V, end=' ')
    visited[V] = 1
    for i in range(1, N+1):
        if visited[i] == 0 and graph[V][i] == 1: ## 방문을 안한 노드일 경우 재귀함수
            dfs(i)

def bfs(V):
    queue = [V]
    visited[V] = 0 ## dfs를 실행했을때 1로 채워졌기 때문에 0으로 변경
    while(queue): # 큐에 원소가 없을 때까지
        V = queue[0]
        print(V, end=' ')
        del queue[0] # 방문 노드 삭제
        for i in range(1, N + 1):
            if visited[i] == 1 and graph[V][i] == 1: # 방문을 안한 노드일 경우 큐에 추가
                queue.append(i)
                visited[i] = 0
dfs(V)
print()
bfs(V)
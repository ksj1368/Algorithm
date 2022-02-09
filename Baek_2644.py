"""
    @ Baek 2644, 촌수계산
    @ Prob. https://www.acmicpc.net/problem/2644
      Ref. 
      Ref Prob. 
    @ Algo: deque
    @ Start day: 22. 01. 28
    @ End day: 22. 01. 28
    탐색 시작 노드로 입력받은 2개의 노드 중 첫 번째 노드를 할당하고 마지막으로 입력 받은 노드로 이동한다.
    이동을 하면서 지나간 간선의 갯수가 촌수, 만약 사로 다른 트리에 있을 경우 -1을 출력
"""

import sys
input = sys.stdin.readline

def dfs(x):
    for i in graph[x]:
        if visit[i] == 0:
            visit[i] = visit[x]+1
            dfs(i)        

n = int(input())
x, y = map(int, input().split())
graph = [[] for _ in range(n+1)]

visit = [0]*(n+1)
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(x)
print(visit[y] if visit[y] > 0 else -1)
"""
    @ Baek 1697, 숨바꼭질
    @ Prob. https://www.acmicpc.net/problem/1697
      Ref. 
      Ref Prob. 
    @ Algo: bfs, deque
    @ Start day: 22. 02. 11
    @ End day: 22. 02. 11
    브루트 포스로 해결하려 했으나 시간이 초과할 것 같아서 너비 우선 탐색으로 문제 풀이
    graph의 범위를 설정하지 않았을 때 런타임 에러가 발생, 따라서 범위를 100001로 선언
    이미 방문한 위치를 다시 방문하는 경우는 최단시간이 아니라서 제외
"""
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(N)
    
    while q:
        x = q.popleft()

        if x == K: ## K에 도착할 경우 도착까지 걸린 시간 출력
            print(graph[x])
            break

        for i in (x+1, x-1, 2*x):
            # 배열의 범위 내에서 방문을 하지 않은 위치일 경우
            if 0 <= i <= len(graph)-1 and not graph[i]: ## len(graph) = 100001이라 -1 
                graph[i] = graph[x] + 1                 ## 이동하는데 걸린 시간을 현재 위치(graph[i])에 저장(이동 횟수 당 + 1)
                q.append(i)

N, K = map(int, input().split())
graph = [0] * 100001
bfs()
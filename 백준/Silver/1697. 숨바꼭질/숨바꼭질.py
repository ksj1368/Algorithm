from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(N)
    
    while q:
        x = q.popleft()
        if x == K:
            print(graph[x])
            break

        for i in (x+1, x-1, 2*x):
            if 0 <= i <= len(graph)-1 and not graph[i]:
                graph[i] = graph[x] + 1
                q.append(i)

N, K = map(int, input().split())
graph = [0] * 100001
bfs()
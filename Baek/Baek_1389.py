"""
    @ Baek 1389, 케빈 베이컨의 6단계 법칙
    @ Prob. https://www.acmicpc.net/problem/1389
      Ref. 
      Ref Prob.
    @ Algo: bfs
    @ Start day: 22. 11. 22
    @ End day: 22. 11. 22
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

def bfs(i):
    cnt = [0]* (n+1)
    visited = [i]
    q = deque()
    q.append(i)
    while q:
        p = q.popleft()
        for j in arr[p]:
            if j not in visited:
                cnt[j] = cnt[p] + 1
                q.append(j)
                visited.append(j)
    return sum(cnt)

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

answer = [0 for _ in range(n+1)]

for i in range(1, n+1):
    answer[i] += bfs(i)
print(answer.index(min(answer[1:-1])))


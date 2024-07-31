"""
    @ Baek 11725, 트리의 부모 찾기
    @ Prob. https://www.acmicpc.net/problem/11725
      Ref. 
      Ref Prob.
    @ Algo: Stack
    @ Start day: 22. 11. 21
    @ End day: 22. 11. 21
"""
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split(" "))
    arr[a].append(b)
    arr[b].append(a)

q = deque()
q.append(1)
answer = [0 for _ in range(n+1)]

def bfs():
    while q:
        x= q.popleft()
        for i in arr[x]:
            if answer[i] == 0:
                answer[i] = x
                q.append(i)
bfs()

for i in range(2, len(answer)):
    print(answer[i])
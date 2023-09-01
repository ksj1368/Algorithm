"""
    @ Baek 1956, 운동
    @ Prob. https://www.acmicpc.net/problem/1956
      Ref. 
      Ref Prob.
    @ Algo: folyd-warshall
    @ Start day: 23. 02. 06
    @ End day: 
"""
import sys
input = sys.stdin.readline

v, e = map(int, input().split(" "))
arr = [[float("inf")] * v for _ in range(v)]

# append value
for _ in range(e):
    a, b, c = map(int, input().split(" "))
    arr[a-1][b-1] = c

# 중간노드에 방문한 값이 더 작을 경우 기존 값보다 작을 경우 방문한 값으로 변경
for i in range(v):
  for j in range(v):
    for k in range(v):
      if arr[i][j] > arr[i][k] + arr[k][j]:
        arr[i][j] = arr[i][k] + arr[k][j]

answer = float("inf")

# 사이클을 돌았다는 것은 출발지와 도착지가 동일하기때문에 arr[i][i]가 최소인 경우를 answer에 저장
for i in range(v):
  answer = min(arr[i][i], answer)
  
if answer == float("inf"):
  print(-1)
else:
  print(answer)
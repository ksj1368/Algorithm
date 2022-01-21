"""
    @ Baek 1021, 회전하는 큐
    @ Prob. https://www.acmicpc.net/problem/1021
      Ref.
      Ref Prob. 
    @ Algo: deque
    @ Start day: 22. 01. 17
    @ End day: 22. 01. 19
"""
import sys
from collections import deque
import itertools
imput = sys.stdin.readline

N, M = map(int, input().split())
deque = deque()
answer = 0

for i in range(1, N+1):
    deque.append(i)

idx = list(map(int, input().split()))

for i in idx:
    point = deque.index(i)
    last_point = len(deque)
    right = list(itertools.islice(deque, point+1, last_point))  # 뽑을 원소부터 마지막 원소까지
    left = list(itertools.islice(deque,0,point))                # 첫 번째 원소부터 뽑을 원소까지
    
    while True :
        if deque[0] == i:               # 덱 첫 번째 원소로 i가 올 경우
            deque.popleft()
            break
        else:
            if len(right) >= len(left): # 왼쪽의 길이가 짧을 경우
                deque.rotate(-1)        # 왼쪽으로 회전
                answer += 1
            else:                       # 오른쪽의 길이가 짧을 경우
                deque.rotate(1)         # 오른쪽으로 회전
                answer += 1
print(answer)
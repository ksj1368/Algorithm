
"""
    @ Baek 10866, 덱
    @ Prob. https://www.acmicpc.net/problem/10866
      Ref. 
      Ref Prob. 
    @ Algo: deque
    @ Start day: 22. 01. 17
    @ End day: 22. 01. 17
    deque의 개념을 알고있으면 쉽게 풀수있는 문제
"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
deque = deque()
for _ in range(N):
    string = input().split()

    if string[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    if string[0] == "pop_back":
         if len(deque) == 0:
            print(-1)
         else:
            print(deque.pop())
    if string[0] == "front":
         if len(deque) == 0:
            print(-1)
         else:
            print(deque[0])
    if string[0] == "back":
         if len(deque) == 0:
            print(-1)
         else:
            print(deque[-1])

    if string[0] == "size":
        print(len(deque))

    if string[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    if string[0] == "push_front":
        deque.appendleft(string[1])
    if string[0] == "push_back":
        deque.append(string[1])
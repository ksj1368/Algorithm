"""
    @ Baek 18258, 큐2
    @ Prob. https://www.acmicpc.net/problem/18258
      Ref. 
      Ref Prob. 
    @ Algo: Queue
    @ Start day: 21. 08. 21
    @ End day: 21. 08. 21
    push, pop, size, empty, top을 함수로 만들어서 함수를 입력하면 해당 함수를 실행
    pop에서 큐에 원소가 있을 경우 첫번째 원소를 출력하고 삭제하는 것을 del로 구현 했을 때
    나머지 원소들이 앞으로 당겨지는데 시간이 소모되기때문에 popleft를 사용
"""

import sys
from collections import deque
input = sys.stdin.readline 
N = int(input())
queue = deque()

def push(i):
    queue.append(i)

def pop(queue):
    if len(queue) == 0:
        print(-1)
    else:
       print(queue.popleft())

def size(queue):
    print(len(queue))

def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front(queue):
    if len(queue) != 0:
        print(queue[0])
    else:
        print(-1)

def back(queue):
    if len(queue) != 0:
        print(queue[-1])
    else:
        print(-1)

for _ in range(N):
    cmd = list(input().split())
    if cmd[0] == 'push':
        push(cmd[1])
    elif cmd[0] == 'pop':
        pop(queue)
    elif cmd[0] == 'size':
        size(queue)
    elif cmd[0] == 'empty':
        empty(queue)
    elif cmd[0] == 'front':
        front(queue)
    elif cmd[0] == 'back':
        back(queue)
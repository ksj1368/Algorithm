"""
    @ Baek 10828, 스택
    @ Prob. https://www.acmicpc.net/problem/10828
      Ref. 
      Ref Prob. 
    @ Algo: Stack
    @ Start day: 21. 08. 16
    @ End day: 21. 08. 16
    push, pop, size, empty, top을 함수로 만들어서 함수를 입력하면 해당 함수를 실행
"""

import sys
input = sys.stdin.readline

N = int(input())
stack = list()

def push(stack,i):
    stack.append(i)

def pop(stack):
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[len(stack)-1])
        del (stack[len(stack)-1])

def size(stack):
    print(len(stack))

def empty(stack):
    if len(stack) == 0:
        print("1")
    else:
        print("0")

def top(stack):
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[len(stack)-1])

for i in range(N):
    cmd = list(input().split())
    
    if cmd[0] == "push":
        push(stack, cmd[1])
    elif cmd[0] == "pop":
        pop(stack)
    elif cmd[0] == "size":
        size(stack)
    elif cmd[0] == "empty":
        empty(stack)
    elif cmd[0] == "top":
        top(stack)

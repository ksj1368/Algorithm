"""
    @ Baek 17608, 막대기
    @ Prob. https://www.acmicpc.net/problem/17608
      Ref.
      Ref Prob. 
    @ Algo: Stack
    @ Start day: 22. 01. 13
    @ End day: 22. 01. 13  
    
"""
import sys
input  =sys.stdin.readline

N = int(input())
stack = [int(input()) for _ in range(N)]
V = stack.pop()
cnt = 1
n = len(stack)
 
for _ in range(n):
    if V < stack[-1]:
        V = stack.pop()
        cnt +=1
    else:
        stack.pop()
print(cnt)
    
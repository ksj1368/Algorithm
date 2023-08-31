"""
    @ Baek 10773, 제로
    @ Prob. https://www.acmicpc.net/problem/10773
      Ref. 
      Ref Prob. 
    @ Algo: Stack
    @ Start day: 21. 08. 17
    @ End day: 21. 08. 17
    
"""
import sys
input = sys.stdin.readline

N = int(input())
stack = list()
for i in range(N):
    num = int(input())
    if num == 0:
        del stack[len(stack)-1]
    else:
        stack.append(num)

print(sum(stack))

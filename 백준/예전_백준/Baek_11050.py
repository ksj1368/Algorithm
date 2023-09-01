"""
    @ Baek 11050, 이항 계수 1
    @ Prob. https://www.acmicpc.net/problem/11050
      Ref. 
      Ref Prob. 
    @ Algo: 
    @ Start day: 22. 01.10
    @ End day: 22. 01. 10
"""
import sys
from math import factorial
input = sys.stdin.readline

N, K = map(int, input().split())
answer = factorial(N) // (factorial(K) * factorial(N-K))
print(answer)
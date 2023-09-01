"""
    @ Baek 2407, 조합
    @ Prob. https://www.acmicpc.net/problem/2407
      Ref. 
      Ref Prob. 
    @ Algo:
    @ Start day: 22. 01. 24
    @ End day: 22. 01. 24
    math 모듈의 factorial 사용
"""
import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
f = math.factorial
print(f(n)//(f(n-m)*f(m)))
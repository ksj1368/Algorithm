"""
    @ Baek 10250, ACM 호텔
    @ Prob. https://www.acmicpc.net/problem/10250
      Ref. 
      Ref Prob. 
    @ Algo: Stack
    @ Start day: 21. 01. 06
    @ End day: 21. 01. 06
"""

import sys  

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    H, W, N = map(int, input().split())
   
    if N%H == 0:
        front_num = H
        back_num = N//H
    else:
         front_num = N%H
         back_num = N//H+1
    print(front_num*100 + back_num)
    
"""
    @ Baek 2231, 분해합
    @ Prob. https://www.acmicpc.net/problem/2231
      Ref. 
      Ref Prob. 
    @ Algo: 브루트 포스
    @ Start day: 21. 05. 18
    @ End day: 21. 05. 18
"""

des = int(input()) 
con = 0
for i in range(1,des+1):
    a = list(map(int, str(i)))
    result = i + sum(a)
    if result == des:
        con = i
        break


print(con)
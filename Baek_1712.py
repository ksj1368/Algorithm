"""
    @ Baek 1712, 손익분기점
    @ Prob. https://www.acmicpc.net/problem/1712
      Ref.
      Ref Prob.
    @ Algo: 
    @ Start day: 21. 04. 30
    @ End day: 21. 04. 30
"""

def BREAK_EVEN_POINT():
    A, B, C = map(int, input().split())
    if B >= C:
        print(-1)
    else: 
        print(int(A/(C-B)+1))

    return 0;
    

BREAK_EVEN_POINT()
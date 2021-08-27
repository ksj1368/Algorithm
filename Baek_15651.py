"""
    @ Baek 15651, N과 M(3)
    @ Prob. https://www.acmicpc.net/problem/15651
      Ref. 
      Ref Prob. 
    @ Algo: 백 트래킹
    @ Start day: 21. 08. 02
    @ End day: 21. 08. 02
    
"""

import sys
n, m = map(int, sys.stdin.readline().split())
out = list()

def prnt(start):
  if len(out) == m:
    print(' '.join(map(str, out)))
    return

  for i in range(1, n+1):
        out.append(i) # 첫 번째 원소 추가
        prnt(start+1) # i+1번째 원소 추가
        out.pop() # 마지막 원소 삭제 

prnt(1)
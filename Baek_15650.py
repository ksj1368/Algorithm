"""
    @ Baek 15650, N과 M(2)
    @ Prob. https://www.acmicpc.net/problem/15650
      Ref. 
      Ref Prob. 
    @ Algo: 백 트래킹, DFS
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

  for i in range(start, n+1):
    if i not in out:
        out.append(i)
        prnt(i+1)
        out.pop()

prnt(1)
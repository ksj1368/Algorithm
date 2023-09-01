"""
    @ Baek 15649, N과 M(1)
    @ Prob. https://www.acmicpc.net/problem/15649
      Ref. 
      Ref Prob. 
    @ Algo: 백 트래킹, DFS
    @ Start day: 21. 07. 31
    @ End day: 21. 07. 31
    리스트의 크기가 m이라면 결과를 출력한다. 선택한 숫자를 다시 선택하면 반복문으로 돌아가서 다시 실행한다. 원소들을 추가하고 prnt()를 실행하고 원소를 제거한다.
"""
import sys
n, m = map(int, sys.stdin.readline().split())
out = list()

def prnt():
  if len(out) == m:
    print(' '.join(map(str, out)))
    return

  for i in range(1, n + 1):
    if i in out:
      continue
    out.append(i)
    prnt()
    out.pop()

prnt()
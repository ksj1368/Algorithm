"""
    @ Baek 11866, 요세프수 문제0
    @ Prob. https://www.acmicpc.net/problem/11866
      Ref.
      Ref Prob.
    @ Algo: deque
    @ Start day: 22. 01. 09
    @ End day: 22. 01. 09  
    deque 사용, rotate로 K만큼 왼쪽으로 이동시켜서 첫 번째 인덱스를 answer에 추가한 뒤 lst에서 제거
"""
import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
answer = []
lst = deque(str(i) for i in range(1, N+1))

while len(lst) != 0:
    lst.rotate(-K)
    answer.append(lst.pop())

print("<",", ".join(answer),">",sep="")

    


"""
    @ Baek 2164, 카드2
    @ Prob. https://www.acmicpc.net/problem/2164
      Ref. 
      Ref Prob. 
    @ Algo: Queue
    @ Start day: 21. 08. 21
    @ End day: 21. 08. 21
   
"""

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
card = deque()
for i in range(1, N+1):
    card.append(i)

while len(card) != 1:
    card.popleft() # 첫번째 카드 제거
    card.append(card.popleft()) # 첫번째 카드를 제거한 뒤를 마지막에 추가 
print(card[0])
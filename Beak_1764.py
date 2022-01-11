"""
    @ Baek 1764, 듣보잡
    @ Prob. https://www.acmicpc.net/problem/1764
      Ref.
      Ref Prob.
    @ Algo: 
    @ Start day: 22. 01. 09
    @ End day: 22. 01. 09  
    set()으로 교집합을 answer에 저장
"""
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
answer = []
N_Listen = [input().strip() for _ in range(N)]
N_See = [input().strip() for _ in range(K)]

answer = list(set(N_Listen) & set(N_See))

answer = sorted(answer)
print(len(answer))
print("\n".join(answer))
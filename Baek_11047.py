"""
    @ Baek 11047, 동전 0
    @ Prob. https://www.acmicpc.net/problem/11047
      Ref.
      Ref Prob.
    @ Algo: greedy algorithm
    @ Start day: 21. 08. 09
    @ End day: 21. 08. 09
"""

import sys
input = sys.stdin.readline
coin = list() 
cnt = 0
N, K = map(int, input().split())    # N = 동전의 개수, K = 값

for i in range(N):                  # 동전의 값 입력
    coin.append(int(input()))

coin.sort(reverse = True)           # 역순 정렬

for i in range(N):
    if coin[i] > K:                 # 동전의 값이 더 클 경우 다음 인덱스로 이동
        continue
    else: 
        x = int(K / coin[i])        # x에 값을 동전의 값으로 나눈 몫을 정수형으로 할당
        K -= x * coin[i]            # 값에 x 와 동전의 값을 곱해준 것을 빼줌
        cnt += x                    # 동전의 개수 추가

print(cnt)
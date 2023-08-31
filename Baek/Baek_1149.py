"""
    @ Baek 1149, RGB 거리
    @ Prob. https://www.acmicpc.net/problem/1149
      Ref. 
      Ref Prob. 
    @ Algo: Dynamic Programming
    @ Start day: 21. 08. 06
    @ End day: 21. 08. 06
    2번째 집부터 반복문을 실행
    2번째 집에서 R, G, B를 선택했을 때 1번째 집에서는 2번째 집에서 선택한 색을 제외하고 남은 색 중 최소값을 가지는 색을 선택하고
    2번째 집에서 선택한 색의 값과 더해준다. 더해준 가격은 2번째 집의 인덱스에 저장하고 이 과정을 모든 집에서 반복한다.
    반복문이 종료되면 3개의 인덱스만 남게 되는데 최소값을 가지는 인덱스를 출력한다.
"""

import sys
input = sys.stdin.readline

N = int(input())
cost = list()

def paint(cost):
    for i in range(1, N):
        cost[i][0] = cost[i][0] + min(cost[i-1][1], cost[i-1][2]) # R
        cost[i][1] = cost[i][1] + min(cost[i-1][0], cost[i-1][2]) # G
        cost[i][2] = cost[i][2] + min(cost[i-1][0], cost[i-1][1]) # B
    print(min(cost[N-1])) 

for i in range(N):
    cost.append(list(map(int, input().split()))) # R G B

paint(cost)

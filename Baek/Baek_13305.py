"""
    @ Baek 13305, 주유소
    @ Prob. https://www.acmicpc.net/problem/13305
      Ref. 
      Ref Prob. 
    @ Algo: greedy
    @ Start day: 21. 08. 14
    @ End day: 21. 08. 14
    무조건 첫 번째 기름 가격으로 도로를 이동해야 한다.
    마지막 기름 가격은 제외
"""
import sys
input = sys.stdin.readline

N = int(input())
road_length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
min = oil_price[0]
result = oil_price[0] * road_length[0]

for i in range(1, N-1):
        if oil_price[i] < min:
            min = oil_price[i]
        result += min*road_length[i]
        
print(result)
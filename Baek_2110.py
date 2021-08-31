"""
    @ Baek 2110, 공유기 설치
    @ Prob. https://www.acmicpc.net/problem/2110
      Ref. 
      Ref Prob. 
    @ Algo: Binaray Search
    @ Start day: 21. 08. 31
    @ End day: 21. 08. 31
"""
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))

house.sort()
left = 1
right = house[-1] - house[0]
answer = 0

while right >= left:
    mid = (right + left) // 2
    before_install = house[0] # 시작점에 공유기 설치
    wifi_cnt = 1              # 시작점에 공유기를 설치했으므로 +1  

    for i in range(1, N):
        if house[i] >= before_install + mid:  # 공유기 설치 간격
            wifi_cnt += 1
            before_install = house[i]

    if wifi_cnt < C:     # 와이파이 개수가 C보다 작으면 더 설치해야 한다. 간격을 좁히자.
        right = mid - 1
   
    else:                # 공유기 개수가 C보다 많거나 같을 경우 설치 간격을 높인다.
        left = mid + 1   # mid를 저장하는 이유는 공유기 설치 개수를 만족할 때 간격을 늘리려다가
        answer = mid     # 개수를 만족시키지 못하고 while문이 종료될 수 있기 때문이다.

print(answer)
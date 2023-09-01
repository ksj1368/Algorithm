"""
    @ Baek 9205, 맥주 마시면서 걸어가기
    @ Prob. https://www.acmicpc.net/problem/9205
      Ref. 
      Ref Prob. 
    @ Algo: BFS
    @ Start day: 22. 04. 03
    @ End day: 22. 04. 03
    50미터를 이동할 때마다 맥주 한병 섭취 하지만 편의점에 도착할 경우 맥주이 개수가 20개로 갱신 되므로 맥주의 개수는 중요하지 않다.
    20*50m 내에 편의점이 있거나 목적지가 있을 경우와 범위 내에 둘다 없을 경우로 나눠서 해결
    for문에서 노드 사이의 거리가 20*50m가 넘지 않을 경우 편의점의 위치(nx, ny)를 현재 위치로 갱신
    목적지(rf_x, rf_y)에 도착할 경우 happy, 도착하지 못할 경우 sad를 출력
"""
import sys
from collections import deque
input = sys.stdin.readline

# BFS(현재 위치)
def BFS(h_x, h_y): 
    q = deque()
    q.append([h_x, h_y])
    while q:
        x, y = q.popleft()

        # 맥주를 다 마시기 전까지 목적지에 도달
        if abs(rf_x - x) + abs(rf_y - y) <= 50 * 20:
            print("happy")
            return

        for i in range(n):
            if visited[i] == 0:     # 편의점을 방문하지 않았을 경우
                nx, ny = cs[i]    # 편의점 위치를 현재 위치로 변경
                
                # 맥주를 다 마시기 전까지 편의점에 도착할 경우
                if abs(nx - x) + abs(ny - y) <= 50 * 20:
                    visited[i] = 1       # 방문 처리
                    q.append([nx, ny])
                    
    # 50*20 범위 내에 경유 할 편의점이 없고 목적지에 도착할 수 없을 경우
    print("sad") 
    return

t = int(input())        # testcase
for _ in range(t):
    n = int(input())        # 편의점 개수
    cs = []                 # 편의점 위치 저장 
    visited = [0] * (n+1)   # 편의점 방문 여부 확인(0 = 미방문, 1 = 방문)
    h_x, h_y = map(int, input().split()) # 시작 위치

    for _ in range(n):
        cs_x, cs_y = map(int, input().split()) # 편의점 위치
        cs.append([cs_x, cs_y])

    rf_x, rf_y = map(int, input().split())     # 페스티벌 위치
    BFS(h_x, h_y)
"""
    @ Baek 11286, 절댓값 힙
    @ Prob. https://www.acmicpc.net/problem/11286
      Ref. 
      Ref Prob. 
    @ Algo: Queue, heap
    @ Start day: 21. 09. 03
    @ End day: 21. 09. 03
    11279, 1927번과 유사
    절댓 값 비교를 위해 abs()사용
"""
import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    i = int(input())
    if i == 0:
        if heap:
            print(heapq.heappop(heap)[1]) 
        else:
            print('0')

    else:
        heapq.heappush(heap, [abs(i), i]) # 절댓 값이 작은 순서대로 heap에 저장
    print(heap)
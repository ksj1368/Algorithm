"""
    @ Baek 1927, 최소 힙
    @ Prob. https://www.acmicpc.net/problem/1927
      Ref. 
      Ref Prob. 
    @ Algo: Queue, heap
    @ Start day: 21. 09. 02
    @ End day: 21. 09. 02
    최대 힙을 구하는 문제에서 22번째 줄에서 [1]을 지우고 26번째 줄에서 [-i, i] 를 i로 수정하면 최소 힙을 구할 수 있다.
"""
import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    i = int(input())
    
    if i == 0:
        if heap: # 힙에 원소가 있을 경우
            print(heapq.heappop(heap)) 
        else: # 힙이 비어있을 경우
            print('0')
    else:
        heapq.heappush(heap, i) 
    print()

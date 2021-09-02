"""
    @ Baek 11279, 최대 힙
    @ Prob. https://www.acmicpc.net/problem/11279
      Ref. 
      Ref Prob. 
    @ Algo: Queue, heap
    @ Start day: 21. 09. 02
    @ End day: 21. 09. 02
    heapq 모듈을 사용했다. heapq 모듈은 최소 힙을 사용하기 때문에 최소 값을 가지는 원소를 출력한다.
    따라서 최대 값을 가지는 원소를 출력 하도록 바꿔줬다.(최대 힙)
    2차원 리스트를 이용해 [i][1]번째 원소 중 최대 값을 가지는 원소를 출력할수 있게 수정했다,
"""
import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    i = int(input())
    
    if i == 0: # '0' 입력
        if heap: # 힙에 원소가 있을 경우
            print(heapq.heappop(heap)[1]) # [i][1]번째 인덱스에 저장된 최대값 출력 후 삭제
        else: # 힙이 비어있을 경우
            print('0')
    else:
        heapq.heappush(heap, [-i, i]) # 2차원 리스트로 저장  
    print()
"""
    @ Baek 1374, 강의실
    @ Prob. https://www.acmicpc.net/problem/1374
      Ref. 
      Ref Prob. 
    @ Algo: 
    @ Start day: 23. 02. 08
    @ End day: 23. 02. 08
"""
# q에 정보 추가(start, end)
# 강의 중인 q에 할당
# 두 번째 강의 이후부터 이전 강의가 끝나지 않은 상태일 경우 새로운 강의실 할당
# 만약 끝난 시간 이후로 강의실이 비어있을 경우에 그 강의실을 현재 강의로 대체

import sys
import heapq
input = sys.stdin.readline

arr = []
n = int(input())
answer = []

for _ in range(n):
    lecture_num, start, end = map(int, input().split(" "))
    heapq.heappush(arr, (start, end))

heapq.heappush(answer, (arr[0][1], arr[0][0])) 
heapq.heappop(arr)

for i in range(1, n):
    start, end = heapq.heappop(arr) # 다음 강의 시작 시간, 끝나는 시간
    lecture_end, lecture_start = heapq.heappop(answer) # 강의 중인 강의의 끝나는 시간, 시작 시간
    
    if lecture_end > start: # 강의중인 강의의 끝나는 시간이 시작할 강의의 시작 시간보다 클 경우
        heapq.heappush(answer, (lecture_end, lecture_start)) # 강의 중인 강의를 현재 강의로 변경
    heapq.heappush(answer, (end, start)) 
    
print(len(answer))
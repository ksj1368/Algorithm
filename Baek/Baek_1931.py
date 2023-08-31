"""
    @ Baek 1931, 회의실 배정
    @ Prob. https://www.acmicpc.net/problem/1931
      Ref.
      Ref Prob. https://suri78.tistory.com/26   
    @ Algo: greedy algorithm
    @ Start day: 21. 08. 09
    @ End day: 21. 08. 09
    틀린 이유 : 빨리 시작하는 순서로 정렬하고 회의가 진행되는 최소 시간으로 고려하지 않았다. 
    따라서 회의가 빨리 끝나는 순서로 정렬해준 뒤 회의가 시작하는 순서대로 정렬해줘야한다.(오름차순)
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*2 for i in range(N)]
end = []
for i in range(N):
    f, s = map(int, input().split())
    arr[i][0] = f
    arr[i][1] = s

arr.sort(key = lambda x : (x[1], x[0])) # 회의가 끝나는 시간 오름차순 정렬, 회의가 시작하는 시간 오름차순 정렬
end = arr[0][1]
cnt = 1
for i in range(1, N):
    if end <= arr[i][0]: # 다음 회의 시작 시간이 이전 회의 끝나는 시간보다 크거나 같을 경우
        cnt += 1
        end = arr[i][1] # 끝나는 시간을 변경

print(cnt)


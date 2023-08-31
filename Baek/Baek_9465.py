"""
    @ Baek 9465, 스티커
    @ Prob. https://www.acmicpc.net/problem/9465
      Ref. 
      Ref Prob. 
    @ Algo: Dynamic Programming
    @ Start day: 22. 01. 24
    @ End day: 22. 01. 24
    선택한 인덱스의 상하좌우를 제외하고 가장 큰 값을 가지는 인덱스를 선택해서 더해줌
    0번째 1번째 행을 동시에 진행하고 각 행의 마지막 인덱스에 도달했을때 큰 값을 가지는 행의 최종 인덱스를 출력
"""
import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    N = int(input())
    arr = []
    dp = []
    for i in range(2):
        arr.append(list(map(int, input().split())))
    for j in range(1, N):
        if j == 1:
            arr[0][1] += arr[1][0]
            arr[1][1] += arr[0][0]
        else:
            arr[0][j] += max(arr[1][j-1], arr[1][j-2])
            arr[1][j] += max(arr[0][j-1], arr[0][j-2])
    print(max(arr[0][N-1], arr[1][N-1]))
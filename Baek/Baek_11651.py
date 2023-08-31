"""
    @ Baek 11651, 좌표 정렬하기2
    @ Prob. https://www.acmicpc.net/problem/11651
      Ref.
      Ref Prob.
    @ Algo: sort
    @ Start day: 21. 07. 29
    @ End day: 21. 07. 29
    16650에서 x 좌표 오름차순 정렬에서 y 좌표를 기준으로 오름차순정렬로 변경
    
"""

import sys
n = int(sys.stdin.readline())
arr = list()
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda y: (y[1], y[0]))  

for i in range(n):
    print(arr[i][0], arr[i][1])

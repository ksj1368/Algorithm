"""
    @ Baek 11650, 좌표 정렬하기
    @ Prob. https://www.acmicpc.net/problem/11650
      Ref.
      Ref Prob.
    @ Algo: sort
    @ Start day: 21. 07. 28
    @ End day: 21. 07. 28
    input() 보다 sys.stdin.readline()가 연산시간이 절약되어 사용
    
"""

import sys
n = int(sys.stdin.readline())
arr = list()
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[0], x[1]))  

for i in range(n):
    print(arr[i][0], arr[i][1])
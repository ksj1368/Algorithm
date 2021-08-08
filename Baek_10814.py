"""
    @ Baek 10814, 나이순 정렬
    @ Prob. https://www.acmicpc.net/problem/10814
      Ref.
      Ref Prob.
    @ Algo: sort
    @ Start day: 21. 07. 29
    @ End day: 21. 07. 29  
    입력 순서는 그대로 유지하고 나이 순으로 정렬(안정 정렬)
"""

import sys
n = int(sys.stdin.readline())
arr = list()

for i in range(n):
    arr.append(sys.stdin.readline().split())

arr.sort(key = lambda x: int(x[0]))

for i in range(len(arr)):
    print(arr[i][0], arr[i][1])

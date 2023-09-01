"""
    @ Baek 1181, 단어 정렬
    @ Prob. https://www.acmicpc.net/problem/1181
      Ref.
      Ref Prob.
    @ Algo: sort
    @ Start day: 21. 07. 29
    @ End day: 21. 07. 29  
    리스트에 원소 추가한 뒤 set으로 바꿈
    중복되는 원소 제거한뒤 리스트로 변경
    먼저 문자열을 사전 순으로 정렬
    정렬된 리스트를 다시 문자의 길이 순으로 정렬
"""

import sys
n = int(sys.stdin.readline())
arr = list()

for i in range(n):
    arr.append(input())

arr = list(set(arr))

arr.sort()
arr.sort(key = len)

for i in range(len(arr)):
    print(arr[i])
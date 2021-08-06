"""
    @ Baek 2751, 수 정렬하기 2
    @ Prob. https://www.acmicpc.net/problem/2751
      Ref.
      Ref Prob.
    @ Algo: 
    @ Start day: 21. 07. 22
    @ End day: 21. 07. 22
    내장함수 sorted 이용
"""

n = int(input())
num = list()

for i in range(n):
    num.append(int(input()))

for i in sorted(num):
    print(i)  
"""
    @ Baek 2750, 수 정렬하기
    @ Prob. https://www.acmicpc.net/problem/2750
      Ref.
      Ref Prob.
    @ Algo: 
    @ Start day: 21. 07. 22
    @ End day: 21. 07. 22
    bubble sort 이용
"""

n = int(input())
num = list()

for i in range(n):
    num.append(int(input()))

for j in range(n):
    for k in range(n):
       if num[j] < num[k]:
           num[j], num[k] = num[k], num[j]
    print(num[j])
"""
    @ Baek 1259, 팰린드롬수
    @ Prob. https://www.acmicpc.net/problem/1259
      Ref.
      Ref Prob.
    @ Algo: 
    @ Start day: 22. 01. 09
    @ End day: 22. 01. 09  

"""
num = list(input())

while num != ['0']:
    if list(reversed(num)) == num:
        print('yes')
    else:
        print('no')
    num = list(input())
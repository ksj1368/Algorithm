"""
    @ Baek 11723, 집합
    @ Prob. https://www.acmicpc.net/problem/11723
      Ref.
      Ref Prob.
    @ Algo: 
    @ Start day: 22. 01. 11
    @ End day: 22. 01. 11 
    n의 길이가 1일때와 1이 아닐 떄로 나눠서 풀었더니 시간초과가 발생하지 않음 길이가 1일때와 아닐 때를 구분하지 않았을 때
    "all"을 입력했을 경우 str형으로 s를 입력했던게 시간 초과의 원인으로 예상
"""
import sys
input = sys.stdin.readline

N = int(input())
s = set()

for _ in range(N):
    n = input().split()
    if len(n) == 1:
        if n[0] == "all":
            s.update(i for i in range(1,21))
        if n[0] == "empty":
            s = set()
    else:
        temp = n[0]
        x = int(n[1])
        if temp == "add":
            s.add(x)
        if temp == "remove":
            s.discard(x)
        if temp == "check":
            print(1 if x in s else 0)
        if temp == "toggle":
            if x in s:
                s.remove(x)
            else:
                s.add(x)
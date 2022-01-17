"""
    @ Baek 1978, 소수 찾기
    @ Prob. https://www.acmicpc.net/problem/1978
      Ref. 
      Ref Prob. 
    @ Algo: 구현
    @ Start day: 22. 01.14
    @ End day: 22. 01. 14
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = map(int,input().split())
answer = 0

for i in arr:
    cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                cnt +=1
        if cnt == 0:
            answer +=1

print(answer)
"""
    @ Baek 17219, 비밀번호 찾기
    @ Prob. https://www.acmicpc.net/problem/17219
      Ref. 
      Ref Prob. 
    @ Algo: 
    @ Start day: 22. 01.12
    @ End day: 22. 01. 12
    2차원 리스트로 사이트와 비밀번호를 입력받고 딕셔너리의 Key에 사이트, value에 비밀번호를 할당
    딕셔너리의 key를 입력받고 value를 출력
"""
import sys
input = sys.stdin.readline
sitenpass = []
d = {}
N, M = map(int,input().split())

for i in range(N):
    sitenpass.append(input().split())
    d[sitenpass[i][0]] = sitenpass[i][1]

for _ in range(M):
    i = str(input().strip())
    print(d[i])


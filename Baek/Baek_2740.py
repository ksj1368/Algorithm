"""
    @ Baek 2740, 행렬 곱셈
    @ Prob. https://www.acmicpc.net/problem/2740
      Ref. 
      Ref Prob. 
    @ Algo: Divide and Conquer
    @ Start day: 21. 08. 25
    @ End day: 21. 08. 25
    행렬의 곱셈만 알고있다면 쉽게 풀수 있다
"""
import sys
input = sys.stdin.readline
A = []
B = []

N, M = map(int, input().split()) # A의 row, col
for i in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split()) # B의 row, col   
for i in range(M):
    B.append(list(map(int, input().split())))

result = [[0 for _ in range(K)] for _ in range(N)] # 결과를 저장할 2차원 리스트 생성

# 행렬의 곱셈 #
for i in range(N):          
    for j in range(K):      
        for k in range(M):
            result[i][j] += A[i][k] * B[k][j] 
# 출력 #
for i in result:
    for j in i:
        print(j, end = ' ')
    print()

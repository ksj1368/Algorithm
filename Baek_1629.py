"""
    @ Baek 1629, 곱셈
    @ Prob. https://www.acmicpc.net/problem/1629
      Ref. 
      Ref Prob. 
    @ Algo: Divide and Conquer
    @ Start day: 21. 08. 24
    @ End day: 21. 08. 24
    처음에는 리스트에 a를 b의 개수만큼 채워준 뒤 절반으로 나누어서 곱해주고 나머지를 구하는 방법으로 답을 구했지만 메모리가 초과했다.
    따라서 모든 연산에서 나머지를 구하는 방법으로 풀었다.
    """

import sys
input = sys.stdin.readline

def sol(b):
    global a, c
    if b == 1: # 길이가 1인 경우( = 결과만 남았을 경우)
        return a%c
    else:
        result = sol(b//2)
        if b%2 == 1:        # 길이가 홀수인 경우
            return result * result * a % c
        else:               # 짝수인 경우
            return result * result % c

a, b, c = map(int, input().split())


print(sol(b))

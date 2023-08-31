"""
    @ Baek 1780, 종이의 개수
    @ Prob. https://www.acmicpc.net/problem/1780
      Ref. 
      Ref Prob. 
    @ Algo: Divide and Conquer
    @ Start day: 21. 08. 24
    @ End day: 21. 08. 24
    1992번, 1780번과 유사한 문제다.
    이번 문제에서는 숫자가 다를 경우 9등분을 해야하기 때문에 2중 for문을 사용해 종이를 나눠줬다.
"""

import sys
input = sys.stdin.readline

def sol(x, y, N):
    global s, minus, zero, one
    clr = s[x][y] # 비교를 위한 색 지정(시작 지점)
    second_break = False # 반복문 탈출

    for i in range(x, x + N):
        if second_break: 
            break
        for j in range(y, y + N):
            if s[i][j] != clr: # 색이 하나라도 다를 경우 재귀함수 실행
                for k in range(3):
                    for l in range(3):
                        sol(x + k*(N//3), y + l*(N//3), N//3)
                second_break = True # 반복문 탈출
                break

    if not second_break: # 탐색을 중단하지 않고 마쳤을 경우
        if s[x][y] == -1:  # '-1'일 경우
            minus += 1
        elif s[x][y] == 1: # '1'일 경우
            one += 1
        else:              # '0'일 경우
            zero +=1

N = int(input())
s = []
minus = 0
zero = 0
one = 0
for _ in range(N):
    s.append(list(map(int, input().split())))

sol(0, 0, N)

print(minus)
print(zero)
print(one)
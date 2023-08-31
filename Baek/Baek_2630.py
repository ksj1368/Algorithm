"""
    @ Baek 2630, 색종이
    @ Prob. https://www.acmicpc.net/problem/2630
      Ref. 
      Ref Prob. 
    @ Algo: Divide and Conquer
    @ Start day: 21. 08. 23
    @ End day: 21. 08. 23
    top-bottom방식으로 풀었다. 
    문제 설명을 읽으면 개념을 쉽게 이해할수 있다. 
    색종이의 색이 다르면 색종이를 4등분한 뒤 다시 색을 비교한다.
    단, 색종이의 색이 모두 흰색 또는 파란색이라면 해당 색종이는 분할을 하지 않는다.
"""

import sys
input = sys.stdin.readline

def sol(x, y, N):
    global blue, white, s
    first = s[x][y] # 비교를 위한 색 지정
    double_break = False #for문 탈출용 double_break

    for i in range(x, x + N):
        if double_break:
            break
        for j in range(y, y + N):
            if s[i][j] != first: # 색이 하나라도 다를 경우 4개의 재귀 함수 실행
                sol(x, y, N//2) # 2사분면
                sol(x + N//2, y, N//2) # 1사분면
                sol(x, y + N//2, N//2) # 3사분면
                sol(x + N//2, y + N//2, N//2) # 4사분면
                double_break = True
                break
            
    if not double_break:
        if s[x][y] == 1: # 파란색일 경우
            blue += 1
        else:            # 흰색일 경우       
            white += 1

N = int(input())
s = []
blue = 0
white = 0

for _ in range(N):
    s.append(list(map(int, input().split())))

sol(0, 0, N)
print(white)
print(blue)
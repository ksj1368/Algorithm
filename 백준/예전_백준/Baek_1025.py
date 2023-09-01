"""
    @ Baek 1025, 제곱수 찾기
    @ Prob. https://www.acmicpc.net/problem/1025
      Ref. 
      Ref Prob. 
    @ Algo: 완탐
    @ Start day: 23. 02. 07
    @ End day: 23. 02. 07
    n과 m의 최대 범위가 9이므로 완전탐색으로 문제를 해결
"""
import sys

answer = -1
n, m = map(int, sys.stdin.readline().split(" "))
arr = []

for _ in range(n):
  arr.append(list(map(int, input())))

# arr의 크기 만큼 탐색
for i in range(n): 
    for j in range(m):
        for row in range(-n, n): # 행 등차
            for col in range(-m, m): # 열 등차
                temp = '' 
                x, y = i, j
                
                # 행과 열이 등차수열일 경우
                if row == 0 and col == 0:
                    continue
                
                while 0<= x <n and 0<= y <m:
                    temp += str(arr[x][y]) # 값 추가
                    if int(temp) ** 0.5 == int(int(temp) ** 0.5): # 루트를 씌운 값의 int형과 float의 값이 같을 경우
                        answer = max(answer, int(temp)) # 큰 값을 answer로 변경
                    # 이동
                    x +=row
                    y +=col
print(answer)
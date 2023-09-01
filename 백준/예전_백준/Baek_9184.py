"""
    @ Baek 9184, 신나는 함수 실행
    @ Prob. https://www.acmicpc.net/problem/9184
      Ref. 
      Ref Prob. 
    @ Algo: 재귀 함수, Dynamic Programming(top-down)
    @ Start day: 21. 08. 04
    @ End day: 21. 08. 04
    Memoization을 사용, 변수가 3개 입력 되므로 3차원 배열을 선언하고 결과를 저장한 뒤 같은 계산을 할 경우 배열의 원소 리턴
"""
import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
      return w(20, 20, 20)

    if alist[a][b][c]: # 배열에 입력한 변수에 해당하는 원소가 있을 경우 리턴
        return alist[a][b][c]

    if a < b and b < c:
      alist[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
      return alist[a][b][c]

    else:   
      alist[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
      return alist[a][b][c]

alist = [[[0]*21 for i in range(21)] for o in range(21)] #  결과를 저장하기 위한 3차원 배열(a, b, c) 선언

while 1:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print("w(%d, %d, %d) = %d" %(a, b, c, w(a,b,c)))
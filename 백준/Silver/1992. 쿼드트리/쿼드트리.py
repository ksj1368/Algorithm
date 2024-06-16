"""
    @ Baek 1912, 쿼드 트리
    @ Prob. https://www.acmicpc.net/problem/1912
      Ref. 
      Ref Prob. 
    @ Algo: Divide and Conquer
    @ Start day: 21. 08. 23
    @ End day: 21. 08. 23
    2630번과 유사
"""
import sys
input = sys.stdin.readline

def QuadTree(x, y, N):
    global s, result
    color = s[x][y] # 비교를 위한 색 지정(시작 지점)
    second_break = False # 반복문 탈출
   

    for i in range(x, x + N):
        if second_break:
            break
        for j in range(y, y + N):
            if s[i][j] != color: # 색이 하나라도 다를 경우 재귀함수 실행
                result += '('
                QuadTree(x, y, N//2)
                QuadTree(x, y + N//2, N//2)
                QuadTree(x + N//2, y, N//2)
                QuadTree(x + N//2, y + N//2, N//2)
                result += ')'
                second_break = True
                break
        
    if not second_break:  
        if s[x][y] == 1:
             result +='1'
        else:
             result+='0'

N = int(input()) # 영상의 크기 입력(N*N)
s = []
result = ''

for _ in range(N):
    s.append(list(map(int, input().rstrip())))

QuadTree(0, 0, N)
print(result)


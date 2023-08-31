"""
    @ Baek 1912, 쿼드 트리
    @ Prob. https://www.acmicpc.net/problem/1912
      Ref. 
      Ref Prob. https://claude-u.tistory.com/269?category=260018
    @ Algo: Divide and Conquer
    @ Start day: 21. 08. 23
    @ End day: 21. 08. 23
    2630번과 동일한 방법으로 풀었다.
    영상을 이루는 픽셀이 모두 흰색 또는 검정색으로만 이루어질 경우 압축을 해서 한줄로 출력한다.
    만약 한 픽셀이라도 색이 다를 경우 영상을 4등분한다. 
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
                QuadTree(x, y, N//2) # 2사분면
                QuadTree(x, y + N//2, N//2) # 1사분면
                QuadTree(x + N//2, y, N//2) # 3사분면
                QuadTree(x + N//2, y + N//2, N//2) # 4사분면
                result += ')'
                second_break = True
                break
        
    if not second_break:  
        if s[x][y] == 1: # 검정색일 경우
             result +='1'
        else:            # 흰색일 경우
             result+='0'

N = int(input()) # 영상의 크기 입력(N*N)
s = []
result = ''

for _ in range(N):
    s.append(list(map(int, input().rstrip())))

QuadTree(0, 0, N)
print(result)

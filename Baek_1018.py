"""
    @ Baek 1018, 체스판 다시 칠하기
    @ Prob. https://www.acmicpc.net/problem/1018
      Ref.
      Ref Prob.
    @ Algo: 
    @ Start day: 21. 05. 22
    @ End day: 21. 05. 22
    윈도우형식으로 미리 8 by 8 체스판을 2가지 케이스로 만들어줬다. 행의 길이만큼 열의 길이에 해당하는 원소를 추가하고
    크고 작음을 비교할 변수를 무한대로 선언해줬다. 윈도우를 사용해서 비교를 해야하니 윈도우에 해당하는 8을 행과 열에서 각각 뺴주고 1을 더해줬다.
    11 23 34  23
"""

st1 = 'BWBWBWBW'
st2 = 'WBWBWBWB'
case1 = [st1, st2, st1, st2, st1, st2, st1, st2]
case2 = [st2, st1, st2, st1, st2, st1, st2, st1]

n, m = map(int, input().split())
chess = []
for i in range(n):
    chess.append(input()) 
rst = float('inf')
for j in range(n-7):
    for k in range(m-7):
        cnt = 0
        for p in range(8):
            for q in range(8):
                if chess[j+p][k+q] != case1[p][q]:
                    cnt +=1
        rst = min(rst, cnt)
        cnt = 0
        for p in range(8):
            for q in range(8):
                if chess[j+p][k+q] != case2[p][q]:
                    cnt +=1
        rst = min(rst, cnt)
print(rst)
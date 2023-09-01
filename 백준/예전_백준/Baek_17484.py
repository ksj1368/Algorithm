"""
    @ Baek 17484, 진우의 달 여행 (Small)
    @ Prob. https://www.acmicpc.net/problem/17484
      Ref.
      Ref Prob.
    @ Algo: DP
    @ Start day: 23. 03. 28
    @ End day: 23. 03. 28
    배열의 최대 크기가 작기 때문에 다이나믹 프로그래밍으로 풀이
    탐색을 진행하는 방향이 3방향으로 정해져 있고 이전과 같은 방향으로 탐색을 진행하지 못한다는 제약조건 때문에 하나의 시작 인덱스는 최대 3개의 결과를 가짐
    따라서 전 탐색을 진행할 3차원 배열을 선언(n by m by 3)
    만약 배열을 벗어날 경우 무한대로 초기화를 하고 배열의 순서대로 진행방향을 정해주고 완전탐색을 진행
    완전 탐색의 결과는 DP의 마지막 열에 저장되어 있으므로 DP의 마지막 열 중에서 최소값을 가지는 인덱스의 값을 출력 
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

dp = [[[0] * 3 for _ in range(m)] for _ in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split())))

for j in range(m):
    for k in range(3):
        dp[0][j][k] = arr[0][j]

# DP 채우기
for i in range(1, n):
    for j in range(m):
        for k in range(3):
            # DP의 범위를 벗어나는 경우
            if (j ==0 and k == 0) or (j == m-1 and k ==2): 
                dp[i][j][k] = float("inf") # 무한대로 초기화
                continue
            if k == 0: # 왼쪽 대각선에서 온 경우
                dp[i][j][k] = arr[i][j] + min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2])
            elif k == 1: # 바로 아래에서 온 경우
                dp[i][j][k] = arr[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])
            else: # 오른쪽 대각선 아래에서 온 경우
                dp[i][j][k] = arr[i][j] + min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1])
                
# 정답 출력
answer = float("inf")
for j in range(m):
    answer = min(answer, min(dp[-1][j]))
print(answer)
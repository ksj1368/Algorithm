"""
    @ Baek 9461, 파도반 수열
    @ Prob. https://www.acmicpc.net/problem/9461
      Ref. 
      Ref Prob. 
    @ Algo: Dynamic Programming
    @ Start day: 21. 08. 05
    @ End day: 21. 08. 05
   가독성을 위해 dp[1]부터 값을 저장했다.
   점화식 활용
"""

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1

def wave(N):
    for i in range(4, N+1):
        dp[i] = dp[i-2] + dp[i-3] # 점화식
    print(dp[N])

for i in range(N):
    wave(int(input()))
"""
    @ Baek 1463, 1로 만들기
    @ Prob. https://www.acmicpc.net/problem/1463
      Ref. 
      Ref Prob. 
    @ Algo: Dynamic Programming
    @ Start day: 22. 04. 03
    @ End day: 22. 04. 03
    배열의 인덱스 번호에 해당 하는 숫자를 1로 만들 때까지 걸린 연산 횟수 할당
    dp(N) = min (dp(N//3) +1, dp(N//2)+1 , dp(N-1)+1), O(n)
    """
import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1) # 연산 횟수 저장용 배열

for x in range(2, n+1):
    dp[x] = dp[x-1] + 1 # 1을 뺌

    if x % 2 == 0: # x가 2로 나누어 떨어질 경우
        dp[x] = min(dp[x], dp[x//2]+1)
    if x % 3 == 0: # x가 3으로 나누어 떨어질 경우
        dp[x] = min(dp[x], dp[x//3] + 1)
   
print(dp[n])
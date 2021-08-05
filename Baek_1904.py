"""
    @ Baek 1904, 01타일
    @ Prob. https://www.acmicpc.net/problem/1904
      Ref. 
      Ref Prob. 
    @ Algo: Dynamic Programming
    @ Start day: 21. 08. 05
    @ End day: 21. 08. 05
    피보나치 수열과 같은 패턴이다.
    24번째 줄에서 15746으로 나눠준 나머지를 출력했더니 메모리가 초과했다.(값이 int 값을 초과하기 때문에 많은 메모리를 차지했기 때문)
    23번째 줄에서 15746으로 나눠줬더니 메모리가 초과하지 않았다.
"""

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 1000001
dp[0] = 1
dp[1] = 2
## 1, 2, 3, 5, 8
def tile(N):
    if N >= 3:
        for i in range(3, N+1):
            dp[i-1] = (dp[i-2]+dp[i-3])%15746
    print(dp[N-1])

tile(N)
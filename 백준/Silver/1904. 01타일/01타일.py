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
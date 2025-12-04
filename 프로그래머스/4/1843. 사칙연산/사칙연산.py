def solution(arr):
    # 1. 숫자와 연산자를 분리하여 저장
    nums = []
    ops = []
    for x in arr:
        if x == '+' or x == '-':
            ops.append(x)
        else:
            nums.append(int(x))
            
    n = len(nums)
    
    # 2. DP 테이블 초기화
    INF = float('inf')
    max_dp = [[-INF] * n for _ in range(n)]
    min_dp = [[INF] * n for _ in range(n)]
    
    # 3. 구간 길이가 1인 경우 초기화
    for i in range(n):
        max_dp[i][i] = nums[i]
        min_dp[i][i] = nums[i]
    
    # 4. step을 1부터 n-1까지 늘려가며 DP 수행
    # step: 현재 묶으려는 숫자의 개수 - 1
    for step in range(1, n):
        for i in range(n - step):
            j = i + step # j: 구간의 끝
            
            # k: 연산자의 위치
            for k in range(i, j):
                operator = ops[k]
                
                if operator == '+':
                    # 최댓값 = 최댓값 + 최댓값
                    # 최솟값 = 최솟값 + 최솟값
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                
                elif operator == '-':
                    # 최댓값 = 최댓값 - 최솟값(가장 큰 수에서 가장 작은 수를 빼야 최대)
                    # 최솟값 = 최솟값 - 최댓값(가장 작은 수에서 가장 큰 수를 빼야 최소)
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j]) 
    return max_dp[0][n-1]
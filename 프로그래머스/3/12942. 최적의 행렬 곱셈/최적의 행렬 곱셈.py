def solution(matrix_sizes):
    matrix_count = len(matrix_sizes)
    # dp[start][end]: start번 행렬부터 end번 행렬까지 곱하는 최소 비용
    dp = [[0] * matrix_count for _ in range(matrix_count)]

    # chain_length: 현재 계산하려는 구간의 길이
    for chain_length in range(2, matrix_count + 1):
        for start_idx in range(matrix_count - chain_length + 1):
            end_idx = start_idx + chain_length - 1
            dp[start_idx][end_idx] = float('inf')
            
            # split_point: 구간을 두 덩어리로 쪼개는 기준점
            # (start_idx 부터 end_idx - 1 까지 자를 수 있음)
            for split_point in range(start_idx, end_idx):
                left_cost = dp[start_idx][split_point]
                right_cost = dp[split_point + 1][end_idx]
                merge_cost = matrix_sizes[start_idx][0] * \
                             matrix_sizes[split_point][1] * \
                             matrix_sizes[end_idx][1]
                total_cost = left_cost + right_cost + merge_cost

                if total_cost < dp[start_idx][end_idx]:
                    dp[start_idx][end_idx] = total_cost
                    
    return dp[0][matrix_count - 1]
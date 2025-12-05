def solution(matrix_sizes):
    matrix_count = len(matrix_sizes)
    # dp[start][end]: start번 행렬부터 end번 행렬까지 곱하는 최소 비용
    dp = [[0] * matrix_count for _ in range(matrix_count)]

    # chain_length: 현재 계산하려는 구간의 길이
    for chain_length in range(2, matrix_count + 1):
        
        # start_idx: 구간의 시작 인덱스
        for start_idx in range(matrix_count - chain_length + 1):
            
            # end_idx: 구간의 끝 인덱스
            end_idx = start_idx + chain_length - 1
            
            # 최소값을 구하기 위해 초기값을 무한대로 설정
            dp[start_idx][end_idx] = float('inf')
            
            # split_point: 구간을 두 덩어리로 쪼개는 기준점
            # (start_idx 부터 end_idx - 1 까지 자를 수 있음)
            for split_point in range(start_idx, end_idx):
                
                # 1. 왼쪽(start ~ split)
                left_cost = dp[start_idx][split_point]
                
                # 2. 오른쪽(split+1 ~ end)
                right_cost = dp[split_point + 1][end_idx]
                
                # 3. 두 덩어리를 합치는 행렬 곱셈 비용 (행 x 공통 x 열)
                # (A행렬의 행) * (분기점 행렬의 열) * (B행렬의 열)
                merge_cost = matrix_sizes[start_idx][0] * \
                             matrix_sizes[split_point][1] * \
                             matrix_sizes[end_idx][1]
                
                # 총 비용 = 왼쪽 해결 비용 + 오른쪽 해결 비용 + 둘을 합치는 비용
                total_cost = left_cost + right_cost + merge_cost
                
                # 최솟값 갱신
                if total_cost < dp[start_idx][end_idx]:
                    dp[start_idx][end_idx] = total_cost
                    
    return dp[0][matrix_count - 1]
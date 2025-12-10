def solution(cookie):
    answer = 0
    n = len(cookie)
    for m in range(n-1):
        l_idx, r_idx = m, m+1
        l_sum, r_sum = cookie[l_idx], cookie[r_idx]
        while True:
           # 동일할 경우 종료
            if l_sum == r_sum:
                answer = max(answer, l_sum)
            # 왼쪽이 작을 경우
            if l_sum <= r_sum and l_idx > 0:
                l_idx -= 1
                l_sum += cookie[l_idx]
            # 오른쪽이 작을 경우
            elif l_sum >= r_sum and r_idx < n -1:
                r_idx += 1
                r_sum += cookie[r_idx]
            # 모두 탐색 또는 범위를 조절할 수 없을 경우
            else:
                break
    return answer
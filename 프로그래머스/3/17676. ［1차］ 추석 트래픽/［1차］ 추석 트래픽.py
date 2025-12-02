from datetime import datetime as dt, timedelta
def solution(lines):
    answer=0    
    logs = []
    for idx, l in enumerate(lines):
        d, t, s = l.split(" ")
        end_t = dt.strptime(d + " " + t, "%Y-%m-%d %H:%M:%S.%f")
        s = float(s[:-1])
        start_t = end_t - timedelta(seconds=s) + timedelta(seconds=0.001)
        logs.append([start_t, end_t])
        
    for i in logs:
        # i번째 로그가 끝나는 시점부터 1초 동안을 검사 범위로 설정
        window_start = i[1]
        window_end = window_start + timedelta(seconds=1)
        cnt = 0
        
        # 1. 로그 시작 시간이 윈도우 끝보다 작아야 함 (window_end 이전에 시작)
        # 2. 로그 종료 시간이 윈도우 시작보다 크거나 같아야 함 (window_start 이후에 끝남)
        for j in logs:
            log_start = j[0]
            log_end = j[1]
            if log_start < window_end and log_end >= window_start:
                cnt += 1
        if answer < cnt:
            answer = cnt
    return answer

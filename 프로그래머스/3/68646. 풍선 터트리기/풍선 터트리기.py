def solution(a):
    if len(a) <= 2:
        return len(a)
    
    # 양 끝 풍선은 무조건 살릴 수 있으므로 2로 시작
    answer = 2 
    
    # 왼쪽 최소값 배열 생성 (l_min[i] = 인덱스 0부터 i까지 중 최솟값)
    l_min = [0] * len(a)
    l_min[0] = a[0]
    for i in range(1, len(a)):
        l_min[i] = min(l_min[i-1], a[i])
        
    # 오른쪽 최소값 배열 생성 (r_min[i] = 인덱스 i부터 끝까지 중 최솟값)
    r_min = [0] * len(a)
    r_min[-1] = a[-1]
    for i in range(len(a)-2, -1, -1):
        r_min[i] = min(r_min[i+1], a[i])
        
    # 양 끝을 제외한 중간 풍선들만 확인 (1 ~ len(a)-2)
    for i in range(1, len(a)-1):
        # 현재 풍선(a[i])이 왼쪽 전체 최소값보다 작거나, 오른쪽 전체 최소값보다 작으면 생존
        # l_min[i-1]: 내 왼쪽까지의 최솟값
        # r_min[i+1]: 내 오른쪽까지의 최솟값
        if a[i] < l_min[i-1] or a[i] < r_min[i+1]:
            answer += 1
            
    return answer
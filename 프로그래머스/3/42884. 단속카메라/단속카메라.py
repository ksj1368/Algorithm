def solution(routes):
    answer = 0
    cam = -30001
    routes.sort(key=lambda x: x[1])
    
    for i in routes:
        if cam < i[0]:
            answer += 1
            cam = i[1]
    return answer
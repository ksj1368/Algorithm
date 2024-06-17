def solution(n):
    answer = []
    arr = [[0] * i for i in range(1, n+1)]
    x, y = -1, 0
    cnt = 1
    
    for i in range(n):
        for j in range(i, n):
            if i%3 == 0: # 아래 이동
                x += 1
            elif i%3 == 1: # 오른쪽 이동
                y += 1
            else: # 위로 이동
                x -= 1
                y -= 1
            arr[x][y] = cnt
            cnt += 1
            
    for i in arr:
        for j in i:
            answer.append(j)
    return answer
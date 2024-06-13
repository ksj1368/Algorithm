# 각 선분 별로 회전을 진행, 시작 지점에 있는 원소를 temp에 저장
def solution(rows, columns, queries):
    answer = []
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    cnt = 1
    
    ## 행렬 생성
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = cnt
            cnt +=1
            
    for x1, y1, x2, y2 in queries:
        x1, x2, y1, y2 = x1-1, x2-1, y1-1, y2-1 
        temp = arr[x1][y1]
        min_value = temp
        
        for i in range(x1, x2):
            arr[i][y1] = arr[i+1][y1]
            min_value = min(min_value, arr[i+1][y1])
        # 아래
        for i in range(y1, y2):
            arr[x2][i] = arr[x2][i+1]
            min_value = min(min_value, arr[x2][i+1])
        # 오른쪽
        for i in range(x2, x1, -1):
            arr[i][y2] = arr[i-1][y2]
            min_value = min(min_value, arr[i-1][y2])
        # 위
        for i in range(y2, y1+1, -1):
            arr[x1][i] = arr[x1][i-1]
            min_value = min(min_value, arr[x1][i-1])
        arr[x1][y1+1] = temp
        answer.append(min_value)
    return answer
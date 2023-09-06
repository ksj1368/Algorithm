def solution(n, lost, reserve):
    answer = n
    arr = [1] * n
    for i in range(n):
        if i+1 in lost:
            arr[i] -= 1
        if i+1 in reserve:
            arr[i] += 1
    
    for i in range(n):
        if i == 0:
            if arr[i] == 0 and arr[i+1] == 2:
                arr[i] = 1
                arr[i+1] = 1
        elif i == n-1:
            if arr[i] == 0 and arr[i-1] == 2:
                arr[i] = 1
                arr[i-1] = 1
        else:
            if arr[i] == 0:
                if arr[i-1] == 2:
                    arr[i] = 1
                    arr[i-1] = 1
                elif arr[i+1] == 2:
                    arr[i] = 1
                    arr[i+1] = 1
    
    for i in arr:
        if i == 0:
            answer -=1
    return answer
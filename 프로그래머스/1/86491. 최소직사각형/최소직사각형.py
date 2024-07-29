def solution(sizes):
    arr = []
    for i in sizes:
        arr.append(sorted(i))
    max_a = arr[0][0]
    max_b = arr[0][1]
    
    for i in range(1, len(arr)):
        if arr[i][0] > max_a:
            max_a = arr[i][0]
        if arr[i][1] > max_b:
            max_b = arr[i][1]
            
    return max_a * max_b
def solution(n): # 1,2,3,5,8 : a_n = a_{n-1} + a_{n-2}

    arr = [0 for _ in range(n)]
    arr[0], arr[1] = 1, 2    
    for i in range(2, n): 
        arr[i] = (arr[i-1] + arr[i-2]) % 1000000007 
    return arr[n-1]
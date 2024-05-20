import sys
n, m = map(int, sys.stdin.readline().split())
check = min(n, m)
arr = []
answer = 0
for i in range(n):
    arr.append(list(sys.stdin.readline()))
    
for i in range(n):
    for j in range(m):
        for k in range(check):
            if ((k+i) < n) and ((j+k)<m) and (arr[i][j] == arr[i+k][j+k] == arr[i+k][j] == arr[i][j+k]):
                answer = max(answer, (k+1)**2)
print(answer)            
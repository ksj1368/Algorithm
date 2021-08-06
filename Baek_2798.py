"""
    @ Baek 2798, 블랙잭
    @ Prob. https://www.acmicpc.net/problem/2798
      Ref. 
      Ref Prob. 
    @ Algo: 브루트 포스
    @ Start day: 21. 05. 15
    @ End day: 21. 05. 15
"""

n, m = map(int, input().split())
a = list(map(int, input().split()))
result = 0
value = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            value = a[i] + a[j] + a[k]      
            if value <= m:
                result = max(result, value)
                   
print(result)
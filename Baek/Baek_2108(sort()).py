"""
    @ Baek 2108, 통계학
    @ Prob. https://www.acmicpc.net/problem/2108
      Ref. 
      Ref Prob. 
    @ Algo: sort
    @ Start day: 21. 07. 27
    @ End day: 21. 07. 27
    리스트를 생성해준 뒤 내장함수 sort를 통해 리스트를 오름차순으로 정렬한 뒤 평균, 중앙값, 최빈값, 범위를 구했다.
"""
import sys
def mode(alist):
    from collections import Counter
    if n == 1 : return alist[0]
    c  = Counter(alist).most_common(2)
    return (c[1][0] if c[0][1] == c[1][1] else c[0][0])

def ran(alist, n):
    if alist[0] == alist[n-1] or n <= 1:
        return 0
    else:    
        return alist[n-1] - alist[0]
    
n = int(input())
alist = []

for i in range(n):
    alist.append(int(sys.stdin.readline()))
alist.sort()

print(round(sum(alist)/n)) # mean
print(alist[n//2]) # median
print(mode(alist))
print(ran(alist, n))

"""
    @ Baek 2108, 통계학
    @ Prob. https://www.acmicpc.net/problem/2108
      Ref. https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-2108%EB%B2%88-%ED%86%B5%EA%B3%84%ED%95%99-in-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
      Ref Prob.
    @ Algo: sort
    @ Start day: 21. 07. 27
    @ End day: 21. 07. 27
    리스트를 생성해준뒤 MergeSort를 통해 리스트를 오름차순으로 정렬한 뒤 평균, 중앙값, 최빈값, 범위를 구했다. 
    출력 결과는 정답과 일치하지만 시간 초과로 인해 sort()를 사용한 코드를 제출했다. 
    입력할 숫자의 개수를 정할 때 입력이 느린 input()을 사용해서 시간 초과가 발생했다.
    input()을 sys.stdin.readline()로 바꾸니 해결됐다.
"""
import sys
def MergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        L = alist[:mid]
        R = alist[mid:]
    
        MergeSort(L)
        MergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                alist[k] = L[i]       
                i += 1
            else:
                alist[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            alist[k] = L[i]
            k += 1
            i += 1

        while j < len(R):
            alist[k] = R[j]
            k += 1
            j += 1
    return alist

def mean(alist,n):
    return round(sum(alist)/n)

def median(alist,n):
    return alist[n//2]

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

MergeSort(alist)
print(mean(alist,n))
print(median(alist,n))
print(mode(alist))
print(ran(alist,n))
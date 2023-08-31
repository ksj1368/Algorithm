"""
    @ Baek 10816, 숫자 카드 2
    @ Prob. https://www.acmicpc.net/problem/10816
      Ref. 
      Ref Prob. 
    @ Algo: Binaray Search
    @ Start day: 21. 08. 26
    @ End day: 21. 08. 27
    맨 아래에 주석 처리한 코드는 이분탐색을 이용했다. 정답은 일치하지만 시간 초과가 발생했다.
    따라서 이분탐색 대신 딕셔너리를 이용해 2중 for문으로 a의 원소가 dic에 포함되면 value를 추가하는 방법으로 풀이했다.
    
"""
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b= list(map(int, input().split()))

dic = dict()

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(m):
    if b[i] in dic:
        print(dic[b[i]], end=' ')
    else:
        print(0, end=' ')
"""
import sys
    input = sys.stdin.readline
    N = int(input())
    a = list(map(int, input().split()))
    M = int(input())
    b = list(map(int, input().split()))
    b_sort = sorted(b)
    result = [0] * M

    def bs(i, b):
        global M
        left = 0
        right = M - 1
    
        while left <= right:
            mid = (left + right)//2
            if b[mid] < i:
                left = mid + 1
            elif b[mid] > i:
                right = mid - 1
            else:
                 return 1
        return 0
            
    for i in range(N):
        bs(a[i], b_sort)
        if bs(a[i], b_sort) == 1:
            result[b.index(a[i])] += 1

    for i in result:
       print(i,end = ' ')
"""
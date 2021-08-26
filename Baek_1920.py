"""
    @ Baek 1920, 수 찾기
    @ Prob. https://www.acmicpc.net/problem/1920
      Ref. 
      Ref Prob. 
    @ Algo: Binaray Search
    @ Start day: 21. 08. 26
    @ End day: 21. 08. 26
    이분 탐색을 할 리스트의 값을 구하고자 하는 값과 비교하여 기준점을 수정할수 있도록 오름차순으로 정렬해준다.
    만약 리스트의 값(mid)이 구하고자 하는 값보다 클 경우 left를 mid의 왼쪽으로 수정해주고 
    작을 경우에는 right를 mid의 오른쪽으로 수정해주면서 리스트 범위을 줄인다.
"""
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort() # 이분 탐색을 하기위해 정렬(오름차순)
    
def bs(A, i): # i = B[i]
    global N, result
    left = 0
    right = N -1
    while left <= right:
        mid = (left + right)//2
        if A[mid] > i:          # B[i]가 A[mid]보다 작을 경우
            right = mid - 1     # right를 수정
        elif A[mid] < i:        # B[i]가 A[mid]보다 클 경우
            left = mid + 1      # left를 수정
        else:                   # B[i] == A[mid]일 경우
            return 1      
    return 0

for i in range(M):
   print(bs(A, B[i]))

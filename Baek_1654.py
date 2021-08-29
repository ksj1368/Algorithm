"""
    @ Baek 1654, 랜선 자르기
    @ Prob. https://www.acmicpc.net/problem/1654
      Ref. 
      Ref Prob. 
    @ Algo: Parametric Search, Binaray Search
    @ Start day: 21. 08. 28
    @ End day: 21. 08. 28
    자르는 길이가 최대 랜선의 길이보다 작거나 같아야 하기 때문에 범위를 1 ~ 랜선의 최대값으로 정한다. 
    자른 랜선의 갯수가 잘라야하는 랜선의 갯수보다 작거나 같을 경우 중앙값의 왼쪽으로 left를 옮겨준다. 
    클 경우에는 중앙값의 오른쪽으로 right를 옮겨준다
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
result = 0
for _ in range(n):
    arr.append(int(input()))

left = 1
right = max(arr)

while left <= right:        # cnt = m 이더라도 최대값이 아닐수 있기 때문에 while문 사용
    cnt = 0
    mid = (left + right)//2
    for i in arr:
        cnt += i//mid       # 랜선 자르기
    if cnt >= m:            # 자른 개수가 잘라야할 개수보다 클 경우 자르는 길이는 mid보다 큰 범위에 있다.
        result = mid        # result를 설정 안하면 mid+1을 출력하므로 result에 저장
        left = mid +1         
    elif cnt < m:           # 자른 개수가 잘라야할 개수보다 작을 경우 자르는 길이는 mid보다 작은 범위에 있다.
        right = mid -1
        
print(result)

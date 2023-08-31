"""
    @ Baek 2805, 나무 자르기
    @ Prob. https://www.acmicpc.net/problem/2805
      Ref. 
      Ref Prob. 
    @ Algo: Binaray Search
    @ Start day: 21. 08. 30
    @ End day: 21. 08. 30
    1654번과 유사
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

#이분탐색 검색 범위 설정
start = 1
end = max(tree) 

# M을 만족하며 최대값을 가지는 절단 길이 찾기
while start <= end: 
    sum_m = 0 # 절단된 나무의 합
    mid = (start+end) // 2
    for i in tree:
        if i >= mid:
            sum_m += i - mid # 나무 길이 - 절단 길이
    
    #벌목 높이를 이분탐색
    if sum_m >= M:           # 절단된 나무의 길이가 M보다 크거나 같을 경우
        start = mid + 1
    else:                    # 절단된 나무의 길이가 M보다 작을 경우
        end = mid - 1

print(end) # 최대 절단 길이
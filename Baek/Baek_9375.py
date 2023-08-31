"""
    @ Baek 9375, 패션왕 신해빈
    @ Prob. https://www.acmicpc.net/problem/9375
      Ref.
      Ref Prob. 
    @ Algo: 
    @ Start day: 22. 01. 15
    @ End day: 22. 01. 15
    문제 해결 방법은 금방 떠올랐지만 코드 구현에 시간을 많이 씀
    내장함수(Counter)로 동일한 단어를 입력하면 개수가 추가하도록 코드 구현
    의상의 조합은 (옷 종류의 개수 +1) + (옷 종류의 개수 +1) - 1
"""
import sys
from collections import Counter
input = sys.stdin.readline

test_case = int(input()) # 테스트 케이스 개수

for _ in range(test_case):
    answer = 1
    n = int(input())    # 옷의 개수
    clothes_type = []   # 옷의 종류를 저장할 리스트

    for _ in range(n):
        clothes = input().split()                # 옷, 옷의 종류
        clothes_type.append(clothes[1])          # 옷의 종류를 리스트에 저장

    clothes_type_cnt = Counter(clothes_type) # 옷의 종류에 따라 개수 세기
        
    for key in clothes_type_cnt:                 # 옷의 조합 계산
        answer *= clothes_type_cnt[key] + 1      # 옷 종류의 개수 +1을 옷의 종류만큼 계산
    print(answer - 1)


        

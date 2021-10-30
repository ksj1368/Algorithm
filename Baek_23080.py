"""
    @ Baek 23080, 스키테일 암호
    @ Prob. https://www.acmicpc.net/problem/23080
      Ref. 
      Ref Prob. 
    @ Algo: greedy
    @ Start day: 21. 10. 30
    @ End day: 21. 10. 30
    줄바꿈 없이 출력할수 있게 print()에서 end = ""를 추가
"""
import sys
input = sys.stdin.readline
K = int(input())
a = str(input())
print(a[0], end = "")
for i in range(K, len(a), K):
    print(a[i], end = "")
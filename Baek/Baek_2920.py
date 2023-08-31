"""
    @ Baek 2920, 음계
    @ Prob. https://www.acmicpc.net/problem/2920
      Ref.
      Ref Prob. 
    @ Algo: 
    @ Start day: 21. 08. 10
    @ End day: 21. 08. 10

"""
import sys
input = sys.stdin.readline


arr = list()
arr = input().split()
cnt = len(arr)
for i in range(1, len(arr)):
    if arr[i-1] < arr[i]:
        cnt += 1
    elif arr[i-1] > arr[i]:
        cnt -= 1

if cnt == 1:
    print("descending")
elif cnt == 2*len(arr) -1 :
    print("ascending")
else:
    print("mixed")
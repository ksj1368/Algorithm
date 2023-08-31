"""
    @ Baek 1431, 시리얼 번호
    @ Prob. https://www.acmicpc.net/problem/1431
      Ref. 
      Ref Prob. 
    @ Algo: sort
    @ Start day: 22. 03. 31
    @ End day: 22. 03. 31
    """
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(input().strip())

for i in range(N-1):
    for j in range(i+1, N): 
        if len(arr[i])>len(arr[j]): # 문자열 길이 비교
            arr[i], arr[j] = arr[j], arr[i]

        elif len(arr[i]) == len(arr[j]):
            sumi = 0
            sumj = 0
            for a, b in zip(arr[i], arr[j]):    # 문자열 숫자 합
                if a.isdigit(): # isdigit() : 
                    sumi +=int(a)
                if b.isdigit():
                    sumj +=int(b)
            if sumi > sumj:
                arr[i],arr[j] = arr[j],arr[i]                
            elif sumi == sumj:                # 문자열의 길이가 같고 문자열 숫자의 합이 같을 경우 사전순으로 정렬  
                for a, b in zip(arr[i], arr[j]):
                    if a > b:
                        arr[i], arr[j] = arr[j], arr[i]
                        break
                    elif a < b:
                        break

for i in arr:
    print(i)

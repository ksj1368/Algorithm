"""
    @ Baek 11399, ATM
    @ Prob. https://www.acmicpc.net/problem/11399
      Ref. 
      Ref Prob. 
    @ Algo: greedy algorithm
    @ Start day: 21. 08. 12
    @ End day: 21. 08. 12
    병합 정렬로 오름차순으로 정렬
    이전 원소들의 합을 누적
    원소들이 합을 출력(각 사람들이 돈을 인출하는데 걸린 총 시간)
"""

import sys
input = sys.stdin.readline

def MergeSort(arr):
    i = j = k = 0
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        MergeSort(left)
        MergeSort(right)

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                arr[k] = right[j]
                j += 1
            else:
                arr[k] = left[i]
                i += 1
            k +=1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j +=1
            k +=1


N = int(input())
arr = [0] * N
arr = list(map(int, input().split()))

MergeSort(arr)

for i in range(1,N):
    arr[i] += arr[i-1]

print(sum(arr))

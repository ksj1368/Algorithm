"""
    @ Baek 1427, 소트인사이드
    @ Prob. https://www.acmicpc.net/problem/1427
      Ref.
      Ref Prob.
    @ Algo: 
    @ Start day: 21. 07. 28
    @ End day: 21. 07. 28
    입력한 정수를 문자열로 바꿈
    문자열를 map()을 사용해 각각의 원소로 나누고 난뒤 다시 정수형으로 변환해 리스트의 원소로 추가
    리스트를 병합 정렬을 통해 내림차순으로 정렬
    정렬한 리스트를 다시 문자열로 변경
    출력 내용을 만족하기 위해 빈 문자열(desc)에 삽입
"""

def merge(arr):
    if len(arr)>1:
  
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
     
        merge(L)
        merge(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j +=1
            k +=1

        while i < len(L):
            arr[k] = L[i]
            k +=1
            i +=1

        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1

    return arr

n = (input())
arr = list(map(int, str(n)))
desc = ''

merge(arr)

for i in range(len(arr)):
    desc += str(arr[i])

print(dsc)
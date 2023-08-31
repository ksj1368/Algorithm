"""
    @ Baek 10989, 수 정렬하기 3
    @ Prob. https://www.acmicpc.net/problem/10989
      Ref. 
      Ref Prob. 
    @ Algo: 정렬
    @ Start day: 22. 01.10
    @ End day: 22. 01. 10
    sorted()를 사용해 리스트를 정렬하면 메모리 초과가 발생한다. 따라서 리스트의 인덱스번호에 해당하는 값을 출력하는 방법을 사용
    입력한 숫자에 해당하는 인덱스에 1을 더해준 뒤 인덱스의 값이 0이 아닐 경우 출력
"""
import sys
input = sys.stdin.readline

N = int(input())
answer = [0 for _ in range(10001)] 

for i in range(N):
    num = int(input())
    answer[num] +=1

for i in range(len(answer)):
    if answer[i] !=0:                ## 0이 아닐경우(값을 입력했을 경우)
        for j in range(answer[i]):   ## 해당하는 인덱스를 출력
            print(i)
        
    
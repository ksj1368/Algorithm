"""
    @ Baek 17298, 오큰수
    @ Prob. https://www.acmicpc.net/problem/17298
      Ref. 
      Ref Prob. https://developmentdiary.tistory.com/240
    @ Algo: Stack
    @ Start day: 21. 08. 20
    @ End day: 21. 08. 20
   이중 for문으로 풀었을때 시간 초과 발생
   결국 풀지 못하고 구글링
"""
import sys 
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = [-1 for _ in range(N)] # 오큰수가 없을 경우 -1을 출력, 따라서 미리 -1로 채워줬다.
stack = []
for i in range(N) :
    while(len(stack) != 0 and arr[stack[-1]] < arr[i]) :    # stack의 길이가 0이 아니고 stack의 탑에 해당하는 인덱스 값이 입력받은 수열보다 작을 경우(stack[-1] = i)
        result[stack[-1]] = arr[i]                          # result[i]의 값(result[stack[-1]])을 arr[i]로 교체
        stack.pop()                                         # stack에서 해당 i를 빼주고 반복
    stack.append(i)

print(*result)
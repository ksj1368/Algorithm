"""
    @ Baek 1874, 스택 수열
    @ Prob. https://www.acmicpc.net/problem/1874
      Ref. 
      Ref Prob. 
    @ Algo: Stack
    @ Start day: 21. 08. 19
    @ End day: 21. 08. 19
    문제를 이해하는데 시간이 걸렸다. 
    num을 입력할때 리스트에 저장을 하고 저장한 리스트의 맨 앞 원소와 스택에 저장된 원소가 같을 경우에 
    num이 저장된 리스트의 첫 번째 원소를 삭제하는 방법으로 해결을 했을 때는 결과는 맞았지만 시간이 초과했다.
    따라서 num을 리스트에 저장하지 않고 num을 입력하는 순간 while문을 통해 num만큼 스택에 원소를 오름차순으로 추가해줬다.
    스택의 마지막 원소가 num과 같을 경우 스택에서 pop해줬다, 만약 num과 같지 않을 경우에는 no에 1를 더해준다.
"""

import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = []
cnt = 1
no = 0
for _ in range(N):
    num = int(input())

    while num >= cnt: # num만금 오름차순으로 stack에 원소 추가
        stack.append(cnt)
        result.append('+')
        cnt +=1

    if stack[-1] == num: # stack의 마지막 원소가 num과 같을경우 pop 아닐경우 no += 1
        stack.pop()
        result.append('-')
    else:
        no +=1

if no >0:
    print("NO")
else:
    for i in result:
        print(i)
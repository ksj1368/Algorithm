"""
    @ Baek 3986, 좋은단어
    @ Prob. https://www.acmicpc.net/problem/3986
      Ref.
      Ref Prob. 
    @ Algo: Stack
    @ Start day: 22. 01. 13
    @ End day: 22. 01. 13
    입력받은 문자열을 하나씩 스택에 저장하고 만약 같은 알파벳이 들어올 경우 스택의 top을 제거
"""
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
for _ in range(N):
    s = input().strip()
    stack = []

    for i in range(len(s)):
        if stack and s[i] == stack[-1]: ## 스택의 top과 s[i]가 같을 경우
            stack.pop()
        else:                           ## 다를 경우 원소 추가
            stack.append(s[i])

    if not stack: # 스택이 공백일 경우
        cnt +=1
print(cnt)
            
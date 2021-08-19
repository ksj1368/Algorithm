"""
    @ Baek 4949, 균형잡힌 세상
    @ Prob. https://www.acmicpc.net/problem/4949
      Ref. 
      Ref Prob. 
    @ Algo: Stack
    @ Start day: 21. 08. 18
    @ End day: 21. 08. 19
    테스트 케이스에 없는 반례를 찾느라 힘들었다 
    line 40에서 cnt == 1을 cnt>0으로 바꿨더니 해결했다.(반례 : ]]] , )])
"""
import sys
input = sys.stdin.readline

while True:
    stack = []
    string = input().rstrip()
    cnt = 0

    if string == ".":
        break

    for i in range(len(string)):
        if string[i] == '[' or string[i] == '(': 
            stack.append(string[i])

        elif len(stack) == 0 and (string[i] == ')' or string[i] == ']'):
            cnt +=1
        elif string[i] == ']':
            if stack[-1] == '[':
                stack.pop()
            elif stack[-1] == '(':
                break

        elif string[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            elif stack[-1] == '[':
                break

    if cnt > 0 or len(stack) != 0:
        print('no')
    else:
        print("yes")

"""
    @ Baek 1459, 걷기
    @ Prob. https://www.acmicpc.net/problem/1459
      Ref. 
      Ref Prob. 
    @ Algo: 
    @ Start day: 22. 10. 16
    @ End day: 22. 10. 16
"""
import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split()) # x+y만큼 이동

if w*2 <= s:
    answer = w*(x+y)
else:
    answer = min(x,y)*s
    if w > s:
        if abs(x-y)%2 == 0:
            answer += abs(x-y)*s
        else:
            answer += (abs(x-y)-1)*s + w
    else:
        answer += abs(x-y)*w
print(answer)

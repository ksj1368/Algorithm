"""
    @ Baek 9012, 괄호
    @ Prob. https://www.acmicpc.net/problem/9012
      Ref. 
      Ref Prob. 
    @ Algo: Stack
    @ Start day: 21. 08. 17
    @ End day: 21. 08. 17
   
"""
import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    VPS = list()
    sum = 0
    test = list(input())
    for j in range(len(test)):
        VPS.append(test[j])
        if VPS[j] == '(':
            sum+= 1
        elif VPS[j] == ')':
            sum -= 1
        if sum < 0:     # ')'가 '('보다 먼저 나올 경우 VPS가 아니므로 sum이 음수일 경우 
            print("NO") # 반복문으로 종료하고 'NO'를 출력
            break

    if sum > 0:         # '('가 많을 경우 VPS가 아니므로
        print("NO")     # 'NO'를 출력
    elif sum == 0:      # '('와 '('의 개수가 같고 ')'가 먼저 나오지 않기 때문에 VPS
        print("YES")    # 'YES' 출력
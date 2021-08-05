"""
    @ Baek 1003, 피보나치 함수
    @ Prob. https://www.acmicpc.net/problem/1003
      Ref. 
      Ref Prob. 
    @ Algo: Dynamic Programming(top-down)
    @ Start day: 21. 08. 03
    @ End day: 21. 08. 03
    f(i-2) + f(i-1) 를 만족하려면 i >= 3 이어야 한다. 따라서 1 ~ 3번째 피보나치 수열의 0, 1의 개수를 리스트에 선언해줬다.
    0을 저장한 리스트의 길이가 피보나치 수열의 정수보다 작거나 같을 경우에 각 리스트 i 번째 원소에 [i -1], [i-2] 번째 원소를 더해준 값을 추가해준다.
    재귀함수를 사용하는 것보다 연산속도가 줄어들었다.
"""
import sys
n = int(sys.stdin.readline())
zero = [1, 0, 1] # f(0), f(1), f(2)의 zero count
one = [0, 1, 1] # f(0), f(1), f(2)의 one count

def fibo(num):
    if len(zero) <= num: # zero의 크기 <= 함수에 입력한 정수 
        for i in range(len(zero), num+1):
            zero.append(zero[i-1] + zero[i-2]) # zero의 마지막 원소로 zero[i-1] + zero[i-2] 추가
            one.append(one[i-1] + one[i-2]) # one의 마지막 원소로 one[i-1] + one[i-2] 추가
    print(zero[num], one[num])

for i in range(n):
    s = int(sys.stdin.readline())
    fibo(s)
